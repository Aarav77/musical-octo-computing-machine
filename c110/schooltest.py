import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd 
import csv

df = pd.read_csv("school1.csv")
data = df["Math_score"].tolist()
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("population mean:- ", mean)
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
def random_set_of_means(counter):
    dataset = []
    for i in range (0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    sd=statistics.stdev(dataset)
    #print("Average = ",mean)
    return mean, sd

def show_fig(mean_list):
    datafile= mean_list
    fig = ff.create_distplot([datafile], ["average"], show_hist=False)
    fig.add_trace(go.Scatter(x=["average", "average"], y=[0, 0.20], mode="lines", name="MEAN"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
    fig.show()

def setup():
      
    
    #Plotting the chart, and lines for mean, 1 standard deviation and 2 standard deviations
    sd_list=[]
    mean_list= []
    for i in range (0,100):
        set_of_means, set_of_sd = random_set_of_means(30)
        mean_list.append(set_of_means)
        sd_list.append(set_of_sd)
    std_deviation_sample=statistics.stdev(mean_list)
    show_fig(mean_list)
    print( "Sampling mean :- ", mean_list[0])
    print( "Standard Deviation of sampling mean :- ", std_deviation_sample)
    Z_score= (mean_list[0]-mean)/std_deviation_sample
    print( "z - Score :- ",Z_score)
    
setup()