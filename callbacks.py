from dash.dependencies import Input, Output

from appt import app


@app.callback(
    Output('page-2-dropdownOUT', 'children'),
    [Input('page-2-dropdown', 'value')])
def display_value(value):
    return 'You have selected the Range Production Number"{}"'.format(value)


@app.callback(
    Output('app-2-display-value', 'children'),
    [Input('app-2-dropdown', 'value')])
def display_value(value):
    return 'You have selected Range Production Number"{}"'.format(value)
