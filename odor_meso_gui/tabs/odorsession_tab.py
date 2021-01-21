from odor_meso_gui.app import app
from datajoint_dashboard.templates import TableBlock
from odor_meso_gui.dj_tables import odor
import dash_html_components as html
import datajoint as dj
from dj_tables import mice
import dash_html_components as html


block = TableBlock(
    odor.OdorSession, app, table_height='600px', table_width='600px',
    extra_tables=[odor.OdorConfig],
    messagebox_style={
                    'width': 490,
                    'height': 50,
                    'marginBottom': '1em',
                    'display': 'block'})


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
