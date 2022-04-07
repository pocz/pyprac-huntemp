import pandas as pd
import sqlalchemy
from sqlalchemy import *

def filldb():
    df = pd.read_csv('huntemp.csv', ';')

    sql_engine = sqlalchemy.create_engine(
        'mysql+mysqldb://huntemp:huntemp@localhost/huntemp'
    )

    my_metadata = sqlalchemy.MetaData()
    monthlies = Table(
        'Monthlies', my_metadata,
            Column('year', Integer, primary_key=True),
            Column('month', Integer, primary_key=True),
            Column('avgt', Numeric(3, 1))
    )
    my_metadata.create_all(sql_engine)

    cxn = sql_engine.connect()
    df.to_sql("Monthlies", cxn, if_exists='append', index=False) 
    cxn.close()

def makedf():
    sql_engine = sqlalchemy.create_engine(
        'mysql+mysqldb://huntemp:huntemp@localhost/huntemp'
    )
    cxn = sql_engine.connect()
    return pd.read_sql_table('Monthlies', cxn)
