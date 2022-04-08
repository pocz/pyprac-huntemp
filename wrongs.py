import huntempdb
import pandas
import pollute

df = huntempdb.makedf()

pollute.pollute(df, 100, 400)
pollute.pollute(df, "bla", 400)

df = df.apply(pandas.to_numeric, errors='coerce')

df['year']= df['year'].where(df['year'] > 1900)
df['month'] = df['month'].mask(df['month'] > 12)
df['avgt'] = df['avgt'].mask(df['avgt'] >50)

df = df.dropna(subset=['year', 'month'])

df['avgt'] = (df['avgt'].ffill()+df['avgt'].bfill())/2
df['avgt'] = df['avgt'].bfill().ffill()
