import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def get_bins(lower_limit, upper_limit, step_size):
    bins = list(range(lower_limit, upper_limit+1, step_size))
    if (upper_limit - lower_limit) % step_size != 0:
        bins.append(upper_limit)
    return bins

df = pd.read_csv("fake_data.csv", header=0)
min_all, max_all = df.min().min(), df.max().max()

bins = get_bins(min_all-1, max_all+1, 10)

'''
Whatever the outcome of the experiment, definitely good experience in trying different graphing options

Two words that plotly seems to rely on:
- Trace
- Marker
'''
#TODO: Set labels
#TODO: Make axis range and ticks the same in both subplots
#TODO: Use custom bins, specified as a list (probably have to use go.Bar for that)

fig = make_subplots(rows=1, cols=2)

fig.add_trace(
    go.Histogram(
        x=df.A,
        name='A',
        opacity=0.75,
        marker = {
            'line' : {
                'color' : 'black',
                'width' : 1
            },
            'color' : '#EB89B5'
        }
        # xbins=bins # This won't work since it needs a dict or XBins object, which forces us to use uniform binning by specifying start, end and size
    ),
    row=1, col=1
)

fig.add_trace(
    go.Histogram(
        x=df.B,
        name='B',
        opacity=0.75,
        marker = {
            'line' : {
                'color' : 'black',
                'width' : 1
            },
            'color' : '#330C73'
        }
    ),
    row=1, col=2
)

# This doesn't ensure the same range
for r in range(1, 2):
    for c in range(1, 3):
        fig.update_xaxes(
            tickmode = 'array',
            tickvals = bins,
            row=r, col=c
        )

fig.show()