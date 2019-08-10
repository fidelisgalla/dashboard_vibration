# -*- coding: utf-8 -*-
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from plotly import graph_objs as go
from app import indicator


#please repair the function (add the list comprehension method)

df=pd.read_excel('vib_data\sample_test_overview.xlsx')
def pie_chart1():
    
    bearing_count = len(df[df['Symptom']=='Bearing'])
    soft_foot = len(df[df['Symptom']=='Soft foot'])
    normal = len(df[df['Symptom']=='Normal'])
    

    layout = go.Layout(
        margin=dict(l=0, r=0, b=0, t=4, pad=8),
        legend=dict(orientation="h"),
        paper_bgcolor="white",
        plot_bgcolor="white",
    )

    trace = go.Pie(
        labels=['Bearing', 'Soft foot','Normal'],
        values=[bearing_count,soft_foot,normal],
        marker={"colors": ["#264e86", "#0074e4", "#74dbef", "#eff0f4"]},
    )

    return {"data": [trace], "layout": layout}
    

layout = [
 
    html.Div(
        [
            html.Br()
        ],
        className="row",
        style={"marginBottom": "5"},
    ),
    # indicators div 
    html.Div(
        [
            indicator(
                "#00cc96",
                "Normal",
                '20'
                ),    
            indicator(
                "#119DFF",
                "Fair",
                '12',
            ),
            indicator(
                "#EF553B",
                "High priority cases",
                '13',
            ),
        ],
        className="row",
    ),


    html.Div(
        [
            html.Div(
                [
                    html.P("Cases Type"),

                    dcc.Graph(
                        id="cases_types",
                        figure = pie_chart1(),
                        config=dict(displayModeBar=False),
                        style={"height": "89%", "width": "98%"},
                    ),

                ],
                className="six columns chart_div",
            ),

            html.Div(
                [
                    html.P("Cases Reasons"),
                    
                    dcc.Graph(
                        id="cases_reasons",
                        figure = pie_chart1(),
                        config=dict(displayModeBar=False),
                        style={"height": "89%", "width": "98%"},
                    ),
                ],
                className="six columns chart_div"
            ),
        ],
        className="row",
        style={"marginTop": "5px"},
    ),


    html.Div(
        [
            html.P()
        ],
        className="row",
        style={"marginTop": "5px"},
    ),
    
]



