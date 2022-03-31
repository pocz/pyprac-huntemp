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
medians_list = []
for x in df['year'].unique():
    yearly_median = df['avgt'][counter:counter+12].median() 
    medians_list.append(yearly_median)
    counter += 12
medians = pd.Series(data=medians_list, index=df['year'].unique())
medians.plot()

plt.gca().set(title='Yearly Median', ylabel= 'Temperature (°C)')
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10.00))
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.50))
plt.gca().xaxis.set_minor_locator(ticker.MultipleLocator(5))
plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(0.25))

plt.show()
