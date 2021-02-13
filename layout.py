from dash_bootstrap_components._components.FormGroup import FormGroup
from dash_bootstrap_components._components.Label import Label
from dash_core_components.Store import Store
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

import util

####### INITIAL ##########
import pandas as pd

# Shouldn't have global data object in Dash apps in general
# But 1) this won't be edited, and 2) later we migth let the user upload their data
df = pd.read_csv("fake_data.csv", header=0)
min_all, max_all = df.min().min(), df.max().max()
lower_limit, upper_limit, stepsize = min_all-1, max_all+1, 10
##########################

layout = html.Div([
    dcc.Store(
        id='data',
        data=df.to_dict('records')
    ),
    html.Div([
        html.H2("Experimenting with Histograms"),
        html.Div([
            html.H5("Choose the desired Bins and click Submit"),
            dbc.Form([
                dbc.FormGroup(
                    [
                        dbc.Label("Start", width=2),
                        dbc.Col(
                            dbc.Input(
                                type='number',
                                id='start-bins',
                                placeholder="Leftmost value on histogram",
                                value=lower_limit
                            ),
                            width=10
                        )
                    ],
                    row=True
                ),
                dbc.FormGroup(
                    [
                        dbc.Label("End", width=2),
                        dbc.Col(
                            dbc.Input(
                                type='number',
                                id='end-bins',
                                placeholder="Rightmost value on histogram",
                                value=upper_limit
                            ),
                            width=10
                        )
                    ],
                    row=True
                ),
                dbc.FormGroup(
                    [
                        dbc.Label("Step Size", width=2),
                        dbc.Col(
                            dbc.Input(
                                type='number',
                                id='step-size-bins',
                                placeholder="Size of each bin",
                                value=stepsize
                            ),
                            width=10
                        )
                    ],
                    row=True
                ),
                dbc.Button(
                    id='update-bins',
                    n_clicks=0,
                    children="Create Bins"
                ),
            ]),

            html.P(),

            dbc.Form([
                dbc.FormGroup(
                    [
                        dbc.Label("Bins", width=2),
                        dbc.Col(
                            dbc.Input(
                                type='list',
                                id='bins',
                                value=str(util.get_bins(lower_limit, upper_limit, stepsize))
                            )
                        )
                    ],
                    row=True
                ),
                dbc.FormText(
                    "You can also manually change the bins above", color="secondary"
                ), html.P(),
                dbc.Button(
                    id='submit-bins',
                    n_clicks=0,
                    children="Submit"
                )
            ]),
        ]), html.P(),

        dcc.Graph(
            id='graph',
            # figure will get updated in first call to callback
        )
    ], className='container')
])

def get_layout():
    return layout