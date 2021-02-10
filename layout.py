from dash_core_components.Store import Store
import dash_html_components as html
import dash_core_components as dcc

####### INITIAL ##########
import pandas as pd

# Shouldn't have global data object in Dash apps in general
# But 1) this won't be edited, and 2) later we migth let the user upload their data
df = pd.read_csv("fake_data.csv", header=0)
min_all, max_all = df.min().min(), df.max().max()

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
        html.H5("Choose the desired Bins and click Submit"),
        
        "Start: ", dcc.Input(
            id='start-bins',
            value=min_all-1,
            type='number'
        ), html.Br(),

        "End: ", dcc.Input(
            id='end-bins',
            value=max_all+1,
            type='number'
        ), html.Br(),

        "Step size: ", dcc.Input(
            id='step-size-bins',
            value=10,
            type='number'
        ), 
        
        html.Button(
            id='update-bins',
            n_clicks=0,
            children="Create Bins"
        ),

        html.P(),

        "Bins: ", dcc.Input(
            id='bins',
            value='',
            type='text',
            style=dict(
                width='550px'
            )
        ), html.P(),

        html.Button(
            id='submit-bins',
            n_clicks=0,
            children="Submit"
        )
    ])
])

def get_layout():
    return layout