import plotly.plotly as py
import plotly.graph_objs as go

trace = go.Scatter(
    x = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],
    y = [0.000067104713439941, 0.0003335237503051758, 0.002768588066101074, 0.020981526374816893, 0.17274521191914877, 
    1.343644094467163, 9.683640917142233, 66.54138526121775, 1900, 15000],
    mode = 'lines',
    name = 'execução'
)

data = [trace]

# Edit the layout
layout = dict(title = 'Tempo de execução por tamanho da matriz', xaxis = dict(title = 'Tamanho'), yaxis = dict(title = 'Tempo'),)

fig = dict(data=data, layout=layout)

py.iplot(fig, filename='styled-line')