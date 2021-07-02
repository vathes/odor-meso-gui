import datajoint as dj
from odor_meso_gui.app import app
from datajoint_dashboard.templates import TableBlock, Filter
from odor_meso_gui.dj_tables import odor, experiment, meso
import dash_html_components as html


def save_tag_query(values):
    return odor.MesoMatch.ScanTag & [{'scan_tag': v} for v in values] if values else {}


def save_tag_options():
    return (odor.MesoMatch.ScanTag & odor.OdorRecording).fetch('scan_tag')

scan_tag_filter = Filter(
    query_function=save_tag_query,
    get_options=save_tag_options,
    filter_id='save-tag-filter',
    filter_name='Save Tag',
    multi=True)

block = TableBlock(odor.OdorRecording, app,
                   extra_tables=[odor.MesoMatch, odor.MesoMatch.ScanTag],
                   filters=[scan_tag_filter])


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
