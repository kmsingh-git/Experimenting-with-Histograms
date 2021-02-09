'''
Simple utility that generates a graph based on data and bins
(Can put other configurables down the line)
'''

import plotly.graph_objects as go
from plotly.subplots import make_subplots

def get_fig(df, bins):
    bins = sorted(bins)
    for i in range(len(bins)-1):
        if bins[i] == bins[i+1]:
            error_msg = f"There are duplicates at indices {i}, {i+1} of sorted bins list"
            assert False, error_msg

    middles, widths, a, b = [], [], [], []

    for i in range(len(bins)-1):
        left, right = bins[i], bins[i+1]
        middles.append((left + right)/2)
        widths.append(right - left)
        
        counts_a = sum((left <= df.A) & (df.A < right))
        counts_b = sum((left <= df.B) & (df.B < right))
        a.append(counts_a)
        b.append(counts_b)

    fig = make_subplots(rows=1, cols=2)

    fig.add_trace(
        go.Bar(
            x=middles,
            y=a,
            width=widths,
            name='A',
            opacity=0.75,
            marker = {
                'line' : {
                    'color' : 'black',
                    'width' : 1
                },
                'color' : '#EB89B5'
            }
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Bar(
            x=middles,
            y=b,
            width=widths,
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
        row=1,
        col=2
    )

    fig.update_layout(
        bargap=0
    )

    return fig