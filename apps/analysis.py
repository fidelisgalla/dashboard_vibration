# -*- coding: utf-8 -

from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from app import fft_plot
from app import app
import pandas as pd
import re
import io  #what is io
import base64  #what is base64

    
layout = [
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
                    dcc.Upload(
                            children=html.Div([
                                    'Drag and Drop .csv file or ',
                                    html.A('Select a File')
                                            ]),
                            style={
                                'width': '100%',
                                'height': '40px',
                                'lineHeight': '60px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '5px',
                                'textAlign': 'center'
                                }
                        ),
                className="eight columns",
                style={"float": "right"},
            ),
            
            #drop down selection for parameter
            html.Div(
               dcc.Dropdown(
                    id="tag_number",
                    options=[
                            {"label": 'NDE-V-VEL',"value": 'NDE_V_VEL'},
                            {"label": 'NDE-H-VEL',"value": 'NDE_H_VEL'},
                            {"label": 'NDE-H-ENV',"value": 'NDE_H_ENV'},
                            {"label": 'DE-V-VEL',"value": 'DE_V_VEL'},
                            {"label": 'DE-H-VEL',"value": 'DE_H_VEL'},
                            {"label": 'DE-H-ENV',"value": 'DE_H_ENV'},
                            {"label": 'DE-H-ACC',"value": 'DE_H_ACC'},
                            {"label": 'DE-A-VEL',"value": 'DE_A_VEL'}
                                                    
                                    ],value = 'NDE_V_VEL',
                    clearable=False, style={"width": "60%"}
                                                
                                ),
               className = "four columns",
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
                    html.P("Vibration Spectrum"),

                    dcc.Graph(
                        id="vibration_spectrum",
                        config=dict(displayModeBar=True),
                        style={"height": "100%", "width": "100%"},
                    ),

                ],
                className="six columns chart_div",
            ),

            html.Div(
                [
                    html.P("Vibration Parameter"),
                    
                     
                    dcc.Graph(
                        id="figure2",
                        config=dict(displayModeBar=True),
                        style={"height": "100%", "width": "100"},
                    ),  
                ],
                className="six columns chart_div"
            ),
        ],
        className="row",
        style={"marginTop": "5px"},
    ),
                                    
]
                     
@app.callback(Output("vibration_spectrum", "figure"), 
              [Input("tag_number", "value"),
              Input("vib_df", "children")],)
def display_vibration_spectrum(option,df):
  #  df=pd.read_csv('vib_data\Export_Spectra1.csv')
    pattern=re.compile(r'"')
    if option == 'NDE_V_VEL':
        spectrum=df.T.iloc[0,0].split(',')
        final_spectrum = [float(re.sub(pattern,'',i)) for i in spectrum[15:] ]
    elif option == 'NDE_H_VEL':
        spectrum=df.T.iloc[0,1].split(',')
        final_spectrum = [float(re.sub(pattern,'',i)) for i in spectrum[15:] ]
    elif option == 'NDE_H_ENV':
        spectrum=df.T.iloc[0,2].split(',')
        final_spectrum = [float(re.sub(pattern,'',i)) for i in spectrum[15:] ]
    elif option == 'NDE_H_ACC':
        spectrum=df.T.iloc[0,4].split(',')
        final_spectrum = [float(re.sub(pattern,'',i)) for i in spectrum[15:] ]
    elif option == 'DE_V_VEL':
        spectrum=df.T.iloc[0,5].split(',')
        final_spectrum = [float(re.sub(pattern,'',i)) for i in spectrum[15:] ]
    elif option == 'DE_H_VEL':
        spectrum=df.T.iloc[0,6].split(',')
        final_spectrum = [float(re.sub(pattern,'',i)) for i in spectrum[15:] ]
    elif option == 'DE_H_ENV':
        spectrum=df.T.iloc[0,7].split(',')
        final_spectrum = [float(re.sub(pattern,'',i)) for i in spectrum[15:] ]
    elif option == 'DE_H_ACC':
        spectrum=df.T.iloc[0,9].split(',')
        final_spectrum = [float(re.sub(pattern,'',i)) for i in spectrum[15:] ]
    else:
        spectrum=df.T.iloc[0,10].split(',')
        final_spectrum = [float(re.sub(pattern,'',i)) for i in spectrum[15:] ]
        
    return fft_plot(final_spectrum)

@app.callback(Output("vib_df", "children"),
              [Input("upload", "contents"),
               Input("upload", "filename")
              ])

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    return df.to_csv('test')

