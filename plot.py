import matplotlib.pyplot as plt
from matplotlib import ticker
import pandas as pd

def bar(df, year):
    fig, ax = plt.subplots()
    sums = df.loc[df['year']==year].isna().sum()
    x = [12-sums['avgt'], sums['avgt']]
    ax.bar(
        ['Valid', 'Na'], x, width=1, edgecolor="white", linewidth=1
    )
    plt.gca().set(title=year)
    plt.tick_params(bottom=False,left=False,labelbottom=False,labelleft=False)
    plt.text(0,-0.5,'Valid',horizontalalignment='center')
    plt.text(1,-0.5,'Na',horizontalalignment='center')
    plt.text(0,-0.8, x[0],horizontalalignment='center')
    plt.text(1,-0.8, x[1],horizontalalignment='center')
    plt.show()

def halves(df):
    first_half = df[:int(len(df)/2)]
    second_half = df[int(len(df)/2):]
    second_half.index = range(len(second_half))
    plt.plot(yearly_means(first_half))
    plt.plot(yearly_means(second_half))
    plt.legend(['1901-1960', '1961-2020'])
    plt.gca().yaxis.set_major_formatter('{x} °C')
    title='Yearly Average Temperatures 1901-1960 and 1961-2020'
    plt.gca().set(title=title)
    plt.show()

def monthly(df):
    plt.plot(df.index, df.avgt, color='tab:red')
    plt.gca().set(
        xlim=(0,len(df)-53), 
        title='Monthly Average Temperature'
    )
    plt.gca().xaxis.set_major_formatter(
        lambda x, pos: str(int(df.loc[int(x)]['year']))
    )
    plt.gca().yaxis.set_major_formatter('{x} °C')
    plt.show()

def seasonal(df, years):
    for i, y in enumerate(years):
        plt.plot('month', 'avgt', data=df.loc[df.year==y])

        year_label_y = df.loc[df.year==y].shape[0]
        year_label_x = df.loc[df.year==y, 'avgt'][-1:].values[0]
        plt.text(year_label_y, year_label_x, y)
    plt.gca().yaxis.set_major_formatter('{x} °C')
    plt.gca().set(
        xlim=(1,12), 
        xlabel='Month'
    )
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(2.00))
    plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(1.00))
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(1.00))
    plt.show()
 
def pie(df, year):
    fig, ax = plt.subplots()
    sums = df.loc[df['year']==year].isna().sum()
    x = [12-sums['avgt'], sums['avgt']]
    ax.pie(
        x, radius=3, center=(4, 4),
        wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True,
        autopct='%d'
    )
    plt.legend(
        ['Valid', 'Na'],
        title="Number of NaN values in:"
    )
    plt.gca().set(title=year)
    plt.tick_params(bottom=False,left=False,labelbottom=False,labelleft=False)
    plt.show()

def yearly_means(df, index=''):
    counter = 0
    means_list = []
    for x in df['year'].unique():
        yearly_mean = df['avgt'][counter:counter+12].mean() 
        means_list.append(yearly_mean)
        counter += 12
    if index == 'year':
        return pd.Series(data=means_list, index=df['year'].unique())
    else:
        return pd.Series(data=means_list, index=range(len(means_list)))

def yearly_medians(df, index=''):
    counter = 0
    medians_list = []
    for x in df['year'].unique():
        yearly_median = df['avgt'][counter:counter+12].mean() 
        medians_list.append(yearly_median)
        counter += 12
    if index == 'year':
        return pd.Series(data=medians_list, index=df['year'].unique())
    else:
        return pd.Series(
            data=medians_list, index=range(len(medians_list))
        )

def yearly_format():
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10.00))
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.50))
    plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(0.25))
