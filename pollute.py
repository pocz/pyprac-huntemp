import pandas
import random

def duplicates(df, count):
    for row in random.sample(list(df.index), k=count):
        top = df.loc[0:row]
        bottom = df.loc[row:]
        top = pandas.concat([top, df.loc[row].to_frame().transpose()], ignore_index=True)
        df = pandas.concat([top, bottom])
        df.index = list(range(len(df)))
    return df

def pollute(df, value, count):
    for row in random.sample(list(df.index), k=count):
        column = random.sample(list(df.columns), k=1)
        df.loc[row, column] = value
