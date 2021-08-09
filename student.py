import csv
import pandas as pd 
import plotly.graph_objects as go
df=pd.read_csv('data.csv')
ID=input('enter student id you was the data for')
student_df=df.loc[df['student_id']==ID]
print('Performance of the Student '+ID+' in the different levels are:',student_df.groupby('level')['attempt'].mean())
fig=go.Figure(go.Bar(
    x=student_df.groupby('level')['attempt'].mean(),
    y=['level 1','level 2','level 3','level 4'],
    orientation='h'
))
fig.update_layout(
    title='<b>Performance of the Student<b> '+ID+'<b> in the different levels are:<b>',
    xaxis_title=" Attempts",
    yaxis_title="Levels",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="orange"
    )
)
fig.show()