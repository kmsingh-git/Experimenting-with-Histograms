import graph

from dash.dependencies import Input, Output, State

import pandas as pd

def get_bins(lower_limit, upper_limit, step_size):
    bins = list(range(lower_limit, upper_limit+1, step_size))
    if (upper_limit - lower_limit) % step_size != 0:
        bins.append(upper_limit)
    return bins

def register_callbacks(app):
    @app.callback(
        Output('bins', 'value'),
        Input('update-bins', 'n_clicks'),
        State('start-bins', 'value'),
        State('end-bins', 'value'),
        State('step-size-bins', 'value')
    )
    def update_bins(_, start, end, stepsize):
        bins = get_bins(start, end, stepsize)
        return str(bins)

    @app.callback(
        Output('graph', 'figure'),
        Input('submit-bins', 'n_clicks'),
        State('bins', 'value'),
        State('data', 'data'),
        prevent_initial_call=True
    )
    def update_graph(_, bins:str, data:dict):
        df = pd.DataFrame(data)

        bins = bins[1:-1].split(', ')
        bins = [float(s) for s in bins]
        
        fig = graph.get_fig(df, bins)

        return fig