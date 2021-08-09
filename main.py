import csv
import pandas as pd 
import plotly.graph_objects as go
df=pd.read_csv('data.csv')
print(df.groupby('level')['attempt'].mean())
fig=go.Figure(go.Bar(
    x=df.groupby('level')['attempt'].mean(),
    y=['level 1','level 2','level 3' ,'level 4'],
    orientation='h'
))
fig.show()