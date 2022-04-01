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

plt.plot(df.index, df.avgt, color='tab:red')

plt.gca().set(
    xlim=(0,len(df)-53), 
    title='Monthly Average',
    ylabel='Temperature (°C)'
)
plt.gca().xaxis.set_major_formatter(
    lambda x, pos: str(int(df.loc[int(x)]['year']))
)

plt.show()
