import graph

from dash.dependencies import Input, Output, State
import util

import pandas as pd

def register_callbacks(app):
    @app.callback(
        Output('bins', 'value'),
        Input('update-bins', 'n_clicks'),
        State('start-bins', 'value'),
        State('end-bins', 'value'),
        State('step-size-bins', 'value')
    )
    def update_bins(_, start, end, stepsize):
        bins = util.get_bins(start, end, stepsize)
        return str(bins)

    @app.callback(
        Output('graph', 'figure'),
        Input('submit-bins', 'n_clicks'),
        State('bins', 'value'),
        State('data', 'data')
    )
    def update_graph(_, bins:str, data:dict):
        df = pd.DataFrame(data)

        bins = bins[1:-1].split(', ')
        bins = [float(s) for s in bins]
        
        fig = graph.get_fig(df, bins)

        return fig