"""Dash App Layout"""
from dash import callback
from dash.dependencies import Input, Output, State

@callback(
    Output('grouprun_output', 'children'),
    Input('submit-button-state', 'n_clicks'),
    State('grouprun_id', 'value'),
    prevent_initial_call=True,)
def update_output(n_clicks, input1):
    return f"Processing data {input1}..."
