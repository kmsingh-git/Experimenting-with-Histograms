from dash_core_components.Store import Store
import dash_html_components as html
import dash_core_components as dcc

####### INITIAL ##########
import pandas as pd

def get_bins(lower_limit, upper_limit, step_size):
    bins = list(range(lower_limit, upper_limit+1, step_size))
    if (upper_limit - lower_limit) % step_size != 0:
        bins.append(upper_limit)
    return bins

# Shouldn't have global data object in Dash apps in general
# But 1) this won't be edited, and 2) later we migth let the user upload their data
df = pd.read_csv("fake_data.csv", header=0)

min_all, max_all = df.min().min(), df.max().max()
bins = get_bins(min_all-1, max_all+1, 10)

##########################

layout = html.Div([
    dcc.Store(
        id='data',
        data=df.to_dict('records')
    ),
    html.H2("Experimenting with Histograms"),
    dcc.Graph(
        id='graph',
        # figure will get updated in first call to callback
    ),
    html.Div([
        "Bins: ",
        dcc.Input(
            id='bins',
            value=str(bins),
            type='text'
        )
    ])
])

def get_layout():
    return layout