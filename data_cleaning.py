import pandas
import random

import huntempdb

def clean_duplicates(df):
    df.drop_duplicates(subset=['year', 'month'], inplace=True)
    return df

def clean_empties(df):
    df['avgt'] = (df['avgt'].ffill()+df['avgt'].bfill())/2
    df['avgt'] = df['avgt'].bfill().ffill()

    df.index = pandas.date_range('1/1901', periods=len(df.index), freq='M')
    df = df.drop(columns=['year', 'month'])

    start_date = pandas.datetime(1901, 1, 31)
    end_date = pandas.datetime(2020, 12, 31)
    daily_date_index = pandas.date_range(
        '31/1/1901', 
        periods=(end_date-start_date).days+1,
        freq='D'
    ) 
    df = df.reindex(daily_date_index)
    df = df['avgt'].interpolate()
    return df

def clean_wrongs(df):
    df = df.apply(pandas.to_numeric, errors='coerce')
    df['year'] = df['year'].where(df['year'] > 1900)
    df['month'] = df['month'].mask(df['month'] > 12)
    df['avgt'] = df['avgt'].mask(df['avgt'] >50)
    df = df.dropna(subset=['year', 'month'])

    df['avgt'] = (df['avgt'].ffill()+df['avgt'].bfill())/2
    df['avgt'] = df['avgt'].bfill().ffill()
    return df

def duplicates(df, count):
    for row in random.sample(list(df.index), k=count):
        top = df.loc[0:row]
        bottom = df.loc[row:]
        top = pandas.concat(
            [top, df.loc[row].to_frame().transpose()], ignore_index=True
        )
        df = pandas.concat([top, bottom])
        df.index = list(range(len(df)))
    return df

def example(mode):
    df = huntempdb.makedf()
    if mode == 'duplicates':
        return clean_duplicates(duplicates(df, 20))
    elif mode == 'empties':
        return clean_empties(pollute(df, None, 700))
    elif mode == 'wrongs':
        return clean_wrongs(wrongs(df)) 
    else:
        return "duplicates/empties/wrongs"

def pollute(df, value, count):
    for row in random.sample(list(df.index), k=count):
        column = random.sample(list(df.columns), k=1)
        df.loc[row, column] = value
    return df

def wrongs(df):
    df = pollute(df, 100, 400)
    df = pollute(df, "bla", 400)
    return df
