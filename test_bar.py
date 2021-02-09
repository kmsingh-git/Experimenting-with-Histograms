import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

df = pd.read_csv("fake_data.csv", header=0)
min_all = df.min().min()
max_all = df.max().max()
bins = list(range(min_all-1, max_all+2, 10))

fig = make_subplots(rows=1, cols=2)

fig.add_trace(
    go.Bar(x=df.A, y=df.B),
    row=1,
    col=1
)

fig.add_trace(
    go.Bar(x=df.B, y=df.A),
    row=1,
    col=2
)

fig.show()