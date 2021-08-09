import pandas as pd
import plotly.express as px
df=pd.read_csv('data2.csv')
fig=px.scatter(df,x='Marks In Percentage',y='Days Present',size='size',color='Roll No',size_max=60)
fig.show()