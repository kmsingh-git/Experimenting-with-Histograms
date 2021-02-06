import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dcc

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    html.H2("Experimenting with Histograms")
])

if __name__ == '__main__':
    app.run_server(debug=True)