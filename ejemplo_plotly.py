import plotly.express as px
import plotly.offline as pyo

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

pyo.plot(fig, filename = "my_plot.html")