import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy
from matplotlib import ticker
from sqlalchemy import create_engine

sql_engine = sqlalchemy.create_engine(
    'mysql+mysqldb://huntemp:huntemp@localhost/huntemp'
)
cxn = sql_engine.connect()
df = pd.read_sql_table('Monthlies', cxn)

plt.figure(dpi=100)

counter = 0
means_list = []
for x in df['year'].unique():
    yearly_mean = df['avgt'][counter:counter+12].mean() 
    means_list.append(yearly_mean)
    counter += 12
means = pd.Series(data=means_list, index=df['year'].unique())
means.plot(color='orange')

plt.gca().set(title='Yearly Mean Temperatures')
plt.gca().yaxis.set_major_formatter('{x} °C')
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10.00))
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.50))
plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

plt.show()
