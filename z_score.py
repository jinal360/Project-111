import statistics
import csv
import random
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["temp"].tolist()
population_mean = statistics.mean(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range (0,100):
        set_of_means = random_set_of_mean(30)
        mean_list .append(set_of_means)
        show_fig(mean_list)

        def show_fig(mean_lsit):
            df = mean_list
            fig = ff.create_displot([df],["temp"], show_hist = False)

            std_deviation = statistics.stdev(mean_list)
            mean = statistics.mean(mean_list)
            print("mean of smapling distribution:-",mean)
            print("Standard deviation of sampling distribution:- ",std_deviation)

            first_std_deviation_start,first_std_deviation_end = mean-std_deviation, mean+std_deviation
            second_std_deviation_start,second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
            third_std_deviation_start,third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

            print("std1",first_std_deviation_start,first_std_deviation_end)
            print("std2",second_std_deviation_start,second_std_deviation_end)
            print("std3",third_std_deviation_start,third_std_deviation_end)

            fig = ff.create_distplot([mean_list],["temp"], show_hist = False)
            fig.add_trace(go.Scatter(x=[mean,mean], y = [0, 0.17], mode = "lines", name = "MEAN"))
            fig.add_trace(go.Scatter(x = [first_std_deviation_start,first_std_deviation_start],y = [0, 0.17], mode = "lines"))
            fig.add_trace(go.Scatter(x = [first_std_deviation_end,first_std_deviation_end],y = [0, 0.17], mode = "lines"))
            fig.add_trace(go.Scatter(x = [second_std_deviation_start,second_std_deviation_start],y = [0, 0.17], mode = "lines"))
            fig.add_trace(go.Scatter(x = [second_std_deviation_end,second_std_deviation_end],y = [0, 0.17], mode = "lines"))
            fig.add_trace(go.Scatter(x = [third_std_deviation_start,third_std_deviation_start],y = [0, 0.17], mode = "lines"))
            fig.add_trace(go.Scatter(x = [third_std_deviation_end,third_std_deviation_end],y = [0, 0.17], mode = "lines"))

            df = pd.read_csv("data2.csv")
            data = df["Maths_score"].tolist()
            new_sample_mean = statistics.mean(data)
            print("mean of sample 2:- ", new_sample_mean)
            fig = ff.create_displot([mean_list], ["temp"], shpw_hist = False)
            fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name="MEAN"))
            fig.add_trace(go.Scatter(x = [new_sample_mean, new_sample_mean], y = [0, 0.17], mode = "lines", name="MEAN OF SAMPLING DATA"))
            fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0, 0.17], mode = "lines", name="FIRST STANDARD DIVEATION"))
            fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0, 0.17], mode = "lines", name="SECOND STANDARD DIVEATION"))

            z_score = (new_sample_mean - sampling_mean)/std_deviation
            print("The z score is = ",z_score)