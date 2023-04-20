import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go

np.random.seed(56)

x_values = np.linspace(0,1,1000)

y_values = np.random.randn(1000)

new_y_values = np.sin(2*np.pi*x_values)

trace1 = go.Scatter(x=x_values, y=y_values, mode='lines', name='data with lines')
trace2 = go.Scatter(x=x_values, y=y_values+5, mode='markers', name='data with markers')
trace3 = go.Scatter(x=x_values, y=y_values-5, mode='lines+markers', name='data with both')
trace4 = go.Scatter(x=x_values, y=new_y_values+5, mode='lines',name='sin func')

data = [
    trace1,trace2,trace3, trace4
]

layout = go.Layout(
    tilte= 'My line plot',
    xaxis = dict(title = 'time'),
    yaxis = dict(title= "something random")
)

fig =go.Figure(data=data, layout=layout)

fig.show()