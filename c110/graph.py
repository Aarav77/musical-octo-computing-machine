import plotly.figure_factory as ff
import statistics
import random
import pandas as pd 
import csv

datafile = pd.read_csv("data.csv")
data =datafile["average"].tolist()
population_mean = statistics.mean(data)
fig = ff.create_distplot([data], ["average"], show_hist=False)
fig.show()