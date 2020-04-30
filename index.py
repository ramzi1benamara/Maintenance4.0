import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from appt import app
from layouts import layout_index, layout1, layout2, layout3, layout4, layout5,layout4a

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return layout1
    elif pathname == '/page-2':
        return layout2
    elif pathname == '/page-3':
        return layout3
    elif pathname == '/page-4a':
        return layout4a
    elif pathname == '/page-4':
        return layout4
    elif pathname == '/page-5':
        return layout5
    else:
        return layout_index


if __name__ == '__main__':
    app.run_server(debug=True)
