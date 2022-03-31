import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

sql_engine = sqlalchemy.create_engine(
    'mysql+mysqldb://huntemp:huntemp@localhost/huntemp'
)
cxn = sql_engine.connect()
df = pd.read_sql_table('Monthlies', cxn)

plt.figure(dpi=100)
for i, y in enumerate(df['year'].unique()):
    plt.plot('month', 'avgt', data=df.loc[df.year==y])

    year_label_y = df.loc[df.year==y].shape[0]
    year_label_x = df.loc[df.year==y,  'avgt'][-1:].values[0]
    plt.text(year_label_y, year_label_x, y)
    
plt.gca().set(
    xlim=(1,12), 
    title='Monthly Averages', 
    ylabel='Temperature (°C)', 
    xlabel='Month'
)

plt.show()
