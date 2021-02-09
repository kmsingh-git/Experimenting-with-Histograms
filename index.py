import dash
import callbacks
import layout



from graph import get_fig

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = layout.get_layout()
callbacks.register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)