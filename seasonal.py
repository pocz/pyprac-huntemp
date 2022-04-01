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
for i, y in enumerate(df['year'].unique()[-5:-1]):
    plt.plot('month', 'avgt', data=df.loc[df.year==y])

    year_label_y = df.loc[df.year==y].shape[0]
    year_label_x = df.loc[df.year==y,  'avgt'][-1:].values[0]
    plt.text(year_label_y, year_label_x, y)
    
plt.gca().set(
    xlim=(1,12), 
    title='Monthly Average Temperatures', 
    xlabel='Month'
)
plt.gca().yaxis.set_major_formatter('{x} °C')
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(2.00))
plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(1.00))
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1.00))

plt.show()
