import graph

from dash.dependencies import Input, Output, State

import pandas as pd

def register_callbacks(app):
    @app.callback(
        Output('graph', 'figure'),
        Input('bins', 'value'),
        State('data', 'data')
    )
    def update_graph(bins:str, data:dict):
        df = pd.DataFrame(data)

        print(df.head())

        bins = bins[1:-1].split(', ')
        bins = [float(s) for s in bins]
        
        fig = graph.get_fig(df, bins)

        return fig