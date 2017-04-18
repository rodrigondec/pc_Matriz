from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# from plotly.graph_objs import Scatter, Figure, Layout
import plotly.graph_objs as go

exe = go.Scatter(
    x = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],
    y = [0.0010001659393310547, 0.0003001570701599121, 0.002151501178741455, 0.016561830043792726, 0.13192821741104127, 1.0577330827713012, 8.66782455444336],
    name = 'execução'
)

read = go.Scatter(
    x = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],
    y = [0.000988006591796875, 0.0020034313201904297, 0.003002643585205078, 0.0030007362365722656, 0.006003141403198242, 0.02101421356201172, 0.08508110046386719],
    name = 'read'
)

prin = go.Scatter(
    x = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],
    y = [0.0, 0.0, 0.002002239227294922, 0.0040035247802734375, 0.014009237289428711, 0.05804038047790527, 0.21515464782714844],
    name = 'print'
)
 
data = [exe, read, prin]

layout = dict(title = 'Tempo de execução por tamanho da matriz', xaxis = dict(title = 'Tamanho da matriz'), yaxis = dict(title = 'Tempo de execução'),)
 
fig = dict(data=data, layout=layout)

plot(fig, filename='grafico_sequencial.html')