from plotly.graph_objs import Scatter, Layout
from plotly import offline
from random_walk import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()
data = [Scatter(x=rw.x_values, y=rw.y_values)]
my_layout = Layout(title='Results of random walk')
offline.plot({'data': data, 'layout': my_layout}, filename='rw.html')