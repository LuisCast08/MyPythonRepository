import numpy as np
import plotly.graph_objects as go
import plotly.offline as pyo

np.random.seed(52)

random_x = np.random.radint(1,101,100)

random_y = np.random.radint(1,101,100)

data = [
    go.scatter(x= random_x,y=random_y, mode = 'markers')
]

layout = go.Layout(
    tiltle = 'My plot'
    xaxis = {title: 'eje_x'}
    yaxis = dict(title= 'eje_y')
    

)

fig = go.Figure(data = data, layout= layout)

fig.show()
