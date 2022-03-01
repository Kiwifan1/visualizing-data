import pandas as pd
import matplotlib.pyplot as plt


def line_chart_example(x_ser, y_ser, min_ser):
    plt.plot(x_ser, y_ser, label="PTS", lw=5, ls="--")
    plt.plot(x_ser, min_ser, label="MIN")


    # lets beautify the plot
    # lets the overlapping x tick labels
    plt.xticks(rotation=25, ha="right")
    plt.xlabel("Players")
    plt.ylabel("PTS Total")
    plt.title("Gonzaga 2021-22 Season Total")
    plt.grid()
    plt.legend()
    # task: add another parameter to our line_chart_example function
    # for the total minutes played
    # and add a line to the chart for total minutes played
    # are points and minutes played related
    
    # right before "rendering" the figure, good to call
    plt.tight_layout()
    # 3 ways to "render" a figure
    # 1. plt.show()
    # create a modal window to interact with the figure
    # plt.show()
    # 2. plt.savefig(path)
    # save the figure to a file (major file types are supported)
    # png, jpg, pdf...
    plt.savefig("line_example.png")
    
    
def scatter_chart_example(x_ser, y_ser):
    plt.figure()
    plt.scatter(x_ser, y_ser, color="red", marker="x", s=200)
    plt.savefig("scatter_example.png")  

def bar_chart_example(x_ser, y_ser):
    plt.figure()
    plt.bar(x_ser, y_ser)
    plt.savefig("bar_example.png")  
    
# call bar_chart_example twice
# 1. pts per player data
# 2. count of each class

def main():
    df = pd.read_csv("bball.csv", index_col=0)
    print(df)

    new_row = pd.Series(["G", 12, 20, 1], index=df.columns)
    new_row.name = "Joe Few"
    df = df.append(new_row)  # use ignore_index = True
    # if no name for hte series
    print(df)

    df["Class"] = ["Sr", "Jr", "Fr", "Fr", "Jr", "Fr",
                   "So", "Fr", "Jr", "Sr", "Fr", "Sr", "Sr", "Fr"]
    print(df)

    class_counts_ser = df["Class"].value_counts()
    print(class_counts_ser)
    grouped_by_class = df.groupby("Class")
    mean_points_ser = grouped_by_class["PTS"].mean()
    print(mean_points_ser)

    ppg_ser = df["PTS"] / df["GP"]
    # lots of ways to do this...
    print(ppg_ser[ppg_ser == ppg_ser.max()])

    # EDA: exploratory data anlysis
    # getting familiar with your data
    # summarizing it using stats, visualizing it
    # mining it for patterns, relationships, groups, etc.

    # goals of data visualization
    # 1. clearly and accurately represent data
    # 2. be creative, with the goal of increasing readability
    # and understanding
    # 3. label axes, units, and points of interest

    # some jargon
    # chart: 2D visualization
    # plot: a chart of data points (e.g. scatter plot)
    # graph: a chart of a math function (e.g. sine curve)

    # we are going to use the matplotlib library for our plotting
    # a few ways to use this
    # 1. pyplot module
    # there is always a "current" figure
    # 2. OOP interface
    # 3. a mix of the #1 and #2
    # we will do #1, and drop down to #3 if we have to

    # let's start with a simple line chart
    # we will show players on the x-axis
    # and PTS on the y-axis
    # note: line chart is not the best way to display
    # continuous data (PTS) grouped by discrete values (players)
    line_chart_example(df.index, df["PTS"], df["MIN"])
    # different chart types
    # 1. scatter
    scatter_chart_example(df.index, df["PTS"])
    # 2. bar
    bar_chart_example(df.index, df["PTS"])
    bar_chart_example(class_counts_ser.index, class_counts_ser)
    # 3. pie
    # 4. histogram
    # 5. (later) box plot


if __name__ == '__main__':
    main()
