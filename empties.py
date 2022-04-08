import huntempdb
import pandas
import pollute

df = huntempdb.makedf()
pollute.pollute(df, None, 700)
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
print(df)
