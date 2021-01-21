import datajoint as dj
from odor_meso_gui.app import app
from datajoint_dashboard.templates import TableBlock
from odor_meso_gui.dj_tables import odor, experiment, meso
import dash_html_components as html

block = TableBlock(odor.OdorRecording, app, extra_tables=[odor.MesoMatch, odor.MesoMatch.ScanTag])


def refresh_contents():
    global tab
    block.construct_layout()
    tab = html.Div(
        className="row app-body",
        children=block.layout
    )


refresh_contents()

if __name__ == '__main__':
    dj.config['safemode'] = False
    app.layout = tab
    app.run_server(debug=True)
