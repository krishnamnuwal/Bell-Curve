##importing all the required modules
import csv
import plotly.figure_factory as ff
import plotly
import pandas as pd 

##storing all the data in the variable file
file=pd.read_csv("data.csv")

##creating an empty list
hist_data=[]

##storing the avg data from to avgRate variable in the form of list
avgRate=file["Avg Rating"].tolist()

##moving to the hist_data list
hist_data.append(avgRate)

##label for graph
label=['AvgRating']

##creating graph
fig=ff.create_distplot(hist_data,label,colors=[' mediumaquamarine'],show_curve=True,curve_type='normal')
plotly.offline.plot(fig)
# print(avgRate)  printing the avg data variable
