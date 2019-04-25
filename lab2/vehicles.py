import matplotlib
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def mad(arr):

    arr = np.ma.array(arr).compressed()  # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))

def get_descriptive_statistics(data):
    print((("Mean: %f") % (np.mean(data))))
    print((("Median: %f") % (np.median(data))))
    print((("Var: %f") % (np.var(data))))
    print((("std: %f") % (np.std(data))))
    print((("MAD: %f") % (mad(data))))


if __name__ == "__main__":
    df = pd.read_csv("vehicles.csv")
    print((df.columns))
    sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)
    sns_plot.axes[0, 0].set_ylim(0, )
    sns_plot.axes[0, 0].set_xlim(0, )
    sns_plot.savefig("scaterplot.png", bbox_inches='tight')
    sns_plot.savefig("scaterplot.pdf", bbox_inches='tight')

    #
    x1 = df.values.T[0]
    get_descriptive_statistics( x1)

    plt.clf()
    sns_plot2 = sns.distplot(x1, bins=20, kde=False, rug=True, label="curent fleet")
    sns_plot2.set_title("histogram")
    sns_plot2.set_ylim(0, 50)
    sns_plot2.set(xlabel='current fleet', ylabel='frequency')
    sns_plot2.get_figure().savefig("current_fleet_histogram.png", bbox_inches='tight')
    sns_plot2.get_figure().savefig("current_fleet_histogram.pdf", bbox_inches='tight')

    x2 = df.dropna().values.T[1]
    get_descriptive_statistics(x2)
    plt.clf()
    sns_plot3 = sns.distplot(x2, bins=20, kde=False, rug=True, label="new fleet")
    sns_plot3.set_title("histogram")
    sns_plot3.set_ylim(0, 50)
    sns_plot3.set(xlabel='New fleet', ylabel='frequency')
    sns_plot3.get_figure().savefig("new_fleet_histogram.png", bbox_inches='tight')
    sns_plot3.get_figure().savefig("new_fleet_histogram.pdf", bbox_inches='tight')




