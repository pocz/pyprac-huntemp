import random

def pollute(df, value, count):
    for row in random.sample(list(df.index), k=count):
        column = random.sample(list(df.columns), k=1)
        df.loc[row, column] = value
