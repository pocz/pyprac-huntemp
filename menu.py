import matplotlib.pyplot as plt
import data_cleaning
import huntempdb
import plot

while True:
    df = huntempdb.makedf()

    print("Menu options:\n \t1: bar graph of number of NaN values per year \n\t2: two halves of yearly means compared \n\t3: seasonal graph of n last years \n\t4: monthly average temperatures \n\t5: pie graph comparing NaN and valid values in n year \n\t6: seasonal graph of the n warmest years \n\t7: yearly mean temperatures \n\t8: yearly median temperatures \n")
    mode = int(input('Enter number of menu option: '))

    if mode == 1:
        year = int(input('Enter the year to display: '))
        plot.bar(data_cleaning.pollute(df, None, 700), year)

    elif mode == 2:
        plot.halves(df) 

    elif mode == 3:
        amount = int(input('Enter number of years to display: '))
        t='Monthly Average Temperatures of The Last {} Years'.format(amount)
        plt.gca().set(title=t)
        plot.seasonal(df, df['year'].unique()[-amount:])

    elif mode == 4:
        plot.monthly(df)

    elif mode == 5:
        year = int(input('Enter the year to display: '))
        plot.pie(data_cleaning.pollute(df, None, 700), year)

    elif mode == 6:
        amount = int(input('Enter number of years to display: '))
        means = plot.yearly_means(df, 'year')
        years = means.sort_values(ascending=False).head(amount).index
        t='Monthly Average Temperatures of The {} Warmest Years'.format(amount)
        plt.gca().set(title=t)
        plot.seasonal(df, years)
 
    elif mode == 7:
        plot.yearly_means(df).plot(color='orange')
        plt.gca().set(title='Yearly Mean Temperatures')
        plt.show()

    elif mode == 8:
        plot.yearly_medians(df).plot(color='orange')
        plt.gca().set(title='Yearly Median Temperatures')
        plt.show()

