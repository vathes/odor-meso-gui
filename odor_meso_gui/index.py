
import datajoint as dj
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from odor_meso_gui.app import app
from odor_meso_gui.tabs import odorant_tab, odorsolution_tab, \
    odorsession_tab, odorrecording_tab

# ========================= Construct webpage layout ========================
app.layout = html.Div(
    [
        dcc.Tabs(
            id="tabs", value='odorant',
            children=[
                dcc.Tab(label='Odorant', value='odorant'),
                dcc.Tab(label='OdorSolution', value='odorsolution'),
                dcc.Tab(label='OdorSession', value='odorsession'),
                dcc.Tab(label='OdorRecording', value='odorrecording'),
            ],
            style={'width': '50%', 'marginBottom': '2em'}),
        html.Div(id='tabs-content')
    ]
)


# ========================= Callback functions =========================
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    current_tab = eval(tab + '_tab')
    current_tab.refresh_contents()
    return current_tab.tab


# ========================= Run server =========================
if __name__ == '__main__':
    dj.config['safemode'] = False
    # run the server, debug = True allows auto-updating without restarting the server.
    app.run_server(host='0.0.0.0', port=8000)
