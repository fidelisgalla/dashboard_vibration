# -*- coding: utf-8 -*-
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
from app import app,insert_data

colors = {"background": "#F3F6FA", "background_div": "white"}


# returns modal (hidden by default)
def modal():

    return html.Div(
        html.Div(
            [
                html.Div(
                    [
                        # modal header
                        html.Div(
                            [
                                html.Span(
                                    "Vibration Record Form",
                                    style={
                                        "color": "#506784",
                                        "fontWeight": "bold",
                                        "fontSize": "20",
                                    },
                                ),
                                html.Span(
                                    "×",
                                    id="cases_modal_close",
                                    n_clicks=0,
                                    style={
                                        "float": "right",
                                        "cursor": "pointer",
                                        "marginTop": "0",
                                        "marginBottom": "17",
                                    },
                                ),
                            ],
                            className="row",
                            style={"borderBottom": "1px solid #C8D4E3"},
                        ),

                        # modal form
                        html.Div(
                            [

                                # left Div
                                html.Div(
                                    [
                                        html.P(
                                            "Tag Name",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        html.Div(
                                            dcc.Dropdown(
                                                id="tag_number",
                                                options=[
                                                    {"label": '220-PM-1A',"value": '220-PM-1A'},
                                                    {"label": '220-PM-1B',"value": '220-PM-1B'},
                                                    {"label": '220-PM-2A',"value": '220-PM-2A'},
                                                    {"label": '220-PM-2B',"value": '220-PM-2B'},
                                                    {"label": '220-PM-3A',"value": '220-PM-3A'},
                                                    {"label": '220-PM-3B',"value": '220-PM-3B'},
                                                    {"label": '220-PM-4A',"value": '220-PM-4A'},
                                                    {"label": '220-PM-4B',"value": '220-PM-4B'}
                                                    
                                                ],
                                                clearable=False,
                                                
                                            )
                                        ),
                                        html.P(
                                            "NDE-V-VEL",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="NDE-V-VEL",
                                            placeholder='NDE-V-VEL (mm/s)',
                                            type= 'text',
                                            value = '',
                                            style = {"width": "100%"}
                                        ),
                                        html.P(
                                            "NDE-H-VEL",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="NDE-H-VEL",
                                            placeholder='NDE-H-VEL (mm/s)',
                                            type= 'text',
                                            value = '',
                                            style = {"width": "100%"}
                                        ),
                                        html.P(
                                            "NDE-H-ENV",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="NDE-H-ENV",
                                            placeholder='NDE-H-ENV (gE)',
                                            type= 'text',
                                            value = '',
                                            style = {"width": "100%"}
                                        ),
                                        html.P(
                                            "NDE-H-ACC",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="NDE-H-ACC",
                                            placeholder='NDE-H-ACC (g)',
                                            type= 'text',
                                            value = '',
                                            style = {"width": "100%"}
                                        ),
                                    ],
                                    className="six columns",
                                    style={"paddingRight": "15"},
                                ),


                                # right Div
                                html.Div(
                                    [
                                        html.P(
                                            "Insert Date",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.DatePickerSingle(
                                                id = "date-picker-modal",
                                                date = dt(2019,1,1),
                                        ),                                        
                                         html.P(
                                            "DE-V-VEL",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="DE-V-VEL",
                                            placeholder='DE-V-VEL (mm/s)',
                                            type= 'text',
                                            value = '',
                                            style = {"width": "100%"}
                                        ),
                                        html.P(
                                            "DE-H-VEL",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="DE-H-VEL",
                                            placeholder='DE-H-VEL (mm/s)',
                                            type= 'text',
                                            value = '',
                                            style = {"width": "100%"}
                                        ),
                                        html.P(
                                            "DE-H-ENV",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="DE-H-ENV",
                                            placeholder='DE-H-ENV (gE)',
                                            type= 'text',
                                            value = '',
                                            style = {"width": "100%"}
                                        ),
                                        html.P(
                                            "DE-H-ACC",
                                            style={
                                                "textAlign": "left",
                                                "marginBottom": "2",
                                                "marginTop": "4",
                                            },
                                        ),
                                        dcc.Input(
                                            id="DE-H-ACC",
                                            placeholder='NDE-H-ACC (g)',
                                            type= 'text',
                                            value = '',
                                            style = {"width": "100%"}
                                        ),
                                    ],
                                    className="six columns",
                                    style={"paddingLeft": "15"},
                                ),
                            ],
                            style={"marginTop": "10", "textAlign": "center"},
                            className="row",
                        ),

                        # submit button
                        html.Span(
                            "Submit",
                            id="submit_new_vib",
                            n_clicks=0,
                            className="button button--primary add"
                        ),

                    ],
                    className="modal-content",
                    style={"textAlign": "center", "border": "1px solid #C8D4E3"},
                )
            ],
            className="modal",
        ),
        id="cases_modal",
        style={"display": "none"},
    )


layout = [

    modal(),
    # top controls
     html.Div(
        [
            
           html.Br()
        ],
        className="row",
        style={"marginBottom": "10"},
    ),
    html.Div(
        [
            
            #add button
            html.Div(
                html.Span(
                    "Add new",
                    id="new_case",
                    n_clicks=0,
                    className="button button--primary add"
                ),
                className="two columns",
                style={"float": "right"},
            ),
        ],
        className="row",
        style={"marginBottom": "10"},
    ),
                                    
    # pie chart for the vibration
    
     html.Div(
        [
            html.Div(
                [
                    html.P("Vibration Parameter"),

                    dcc.Graph(
                        id="vibration_parameter1",
                        config=dict(displayModeBar=False),
                        style={"height": "89%", "width": "98%"},
                    ),

                ],
                className="six columns chart_div",
            ),

            html.Div(
                [
                    html.P("Vibration Parameter2"),
                    
                     dcc.Dropdown(
                            id="tag_number",
                            options=[
                                    {"label": '220-PM-1A',"value": '220-PM-1A'},
                                    {"label": '220-PM-1B',"value": '220-PM-1B'},
                                    {"label": '220-PM-2A',"value": '220-PM-2A'},
                                    {"label": '220-PM-2B',"value": '220-PM-2B'},
                                    {"label": '220-PM-3A',"value": '220-PM-3A'},
                                    {"label": '220-PM-3B',"value": '220-PM-3B'},
                                    {"label": '220-PM-4A',"value": '220-PM-4A'},
                                    {"label": '220-PM-4B',"value": '220-PM-4B'}
                                                    
                                    ],clearable=False, style={"width": "60%"}
                                                
                                ),
    
                    
                    dcc.DatePickerRange(
                            id='date-picker-range',
                            min_date_allowed=dt(2018, 1, 1),
                            max_date_allowed=dt(2025, 1, 1),
                            initial_visible_month=dt(2019,1,1),
                            end_date=dt(2019, 1,1), 
                                     ),
                            
                    
                    dcc.Graph(
                        id="vibration_parameter2",
                        config=dict(displayModeBar=False),
                        style={"height": "90%", "width": "80"},
                    ),  
                ],
                className="six columns chart_div"
            ),
        ],
        className="row",
        style={"marginTop": "5px"},
    ),
                        
]

@app.callback(Output("cases_modal", "style"), [Input("new_case", "n_clicks")])
def display_cases_modal_callback(n):
    if n > 0:
        return {"display": "block"}
    return {"display": "none"}


@app.callback(
    Output("new_case", "n_clicks"),
    [Input("cases_modal_close", "n_clicks"), Input("submit_new_vib", "n_clicks")],
)
def close_modal_callback(n, n2):
    return 0

@app.callback(
    Output("vibration", "children"),
    [Input("submit_new_vib", "n_clicks")],
    [
        State("tag_number", "value"),
        State("date-picker-modal", "date"),
        State("NDE-V-VEL", "value"),
        State("NDE-H-VEL", "value"),
        State("NDE-H-ENV", "value"),
        State("NDE-H-ACC", "value"),
        State("DE-V-VEL", "value"),
        State("DE-H-VEL", "value"),
        State("DE-H-ENV", "value"),
        State("DE-H-ACC", "value"),
        State("Vibration","value")
    
    ])
def add_vib_data(
    n_clicks, tag, date, nde_v_vel, nde_h_vel, nde_h_env, nde_h_acc, de_v_vel, de_h_vel,de_h_env,de_h_acc,vibration
):
    if n_clicks > 0:
        query = {
            "Tag": tag,
            "Date" : date,
            "NDE-V-VEL" : nde_v_vel,
            "NDE-H-VEL" : nde_h_vel,
            "NDE-H-ENV" : nde_h_env,
            "NDE-H-ACC" : nde_h_acc,
            "DE-V-VEL" : de_v_vel,
            "DE-H-VEL" : de_h_vel,
            "DE-H-ENV" : de_h_env,
            "DE-H-ACC" : de_h_acc,
            
        }
        
        insert_data(query)
    return vibration
 

    


