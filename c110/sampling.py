import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd 
import csv

def random_set_of_means(counter):
    datafile = pd.read_csv("medium_data.csv")
    data =datafile["reading_time"].tolist()
    dataset = []
    for i in range (0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    datafile= mean_list
    fig = ff.create_distplot([datafile], ["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x=["reading_time", "reading_time"], y=[0, 12], mode="lines", name="MEAN"))
    fig.show()

def setup():
    mean_list= []
    for i in range (0,1000):
        set_of_means = random_set_of_means(100)
        mean_list.append(set_of_means)
    sd=statistics.stdev(mean_list)
    print("standard deviation of sampling mean: ", sd)
    show_fig(mean_list)

setup()