import datajoint as dj
from costagui_demos.app import app
from costagui_demos.tab_templates import TableBlock


subject_table_tab = TableBlock(subject.Subject, app)


if __name__ == '__main__':
    dj.config['safemode'] = False
    app.layout = subject_table_tab.layout
    app.run_server(debug=True)
