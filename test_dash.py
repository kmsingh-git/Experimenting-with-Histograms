import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

import random

'''
Use this is a testing ground for Dash stuff
'''

app = dash.Dash(__name__)

app.layout = html.Div([])

@app.callback(
    
)
def _():
    pass

if __name__ == '__main__':
    app.run_server(debug=True)