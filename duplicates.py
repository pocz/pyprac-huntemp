import huntempdb
import pollute

df = huntempdb.makedf()
df = pollute.duplicates(df, 20)

df.drop_duplicates(subset=['year', 'month'], inplace=True)
