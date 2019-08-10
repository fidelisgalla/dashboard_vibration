import flask
import dash
import dash_html_components as html
#import dash_core_components as dcc
#from datetime import datetime as dt
import mysql.connector
import MySQLdb
from MySQLdb import Error
from plotly import graph_objs as go
import numpy as np

#connection to flask
server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)
app.config.suppress_callback_exceptions = True




#returns top indicator div
def indicator(color, text, id_value):
    return html.Div(
        [
            
            html.P(
                text,
                className="twelve columns indicator_text"
            ),
            html.P(
                id = id_value,
                className="indicator_value"
            ),
        ],
        className="four columns indicator",
        
    )

#create table 
def create_table():
    try:
        connection = MySQLdb.connect(host='localhost',
                             database='classicmodels',
                             user='root',
                             password='1807fidel'
                            )
        cursor=connection.cursor()
        if connection.is_connected():
            print ('connection success')
   
    except Error as e :
        print ("Error while connecting to MySQL", e)

    TABLES= (
            "CREATE TABLE MOTOR_TEST("
            "  NUMBER int(11) NOT NULL AUTO_INCREMENT,"
            "  TAG CHAR(20) NOT NULL,"
            "  DATE date NOT NULL,"
            "  NDE_V_VEL FLOAT,"
            "  NDE_H_VEL FLOAT,"
            "  NDE_H_ENV FLOAT,"
            "  NDE_H_ACC FLOAT,"
            "  DE_V_VEL FLOAT,"
            "  DE_H_VEL FLOAT,"
            "  DE_H_ENV FLOAT,"
            "  DE_H_ACC FLOAT,"
            "  PRIMARY KEY (NUMBER)"
            " ) ") 
    try:
        print("Creating table {}: ".format('MOTOR_TEST'), end='')
        cursor.execute(TABLES)
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
    
    connection.close()

def insert_data(query):
    try:
        connection = MySQLdb.connect(host='localhost',
                             database='classicmodels',
                             user='root',
                             password='1807fidel'
                            )
        cursor=connection.cursor()
        if connection.is_connected():
            print ('connection success')
   
    except Error as e :
        print ("Error while connecting to MySQL", e)
    
    add_vibration_data= ("INSERT INTO MOTOR1"
                    "(TAG, DATE, NDE_V_VEL,NDE_H_VEL,NDE_H_ENV,NDE_H_ACC,"
                     "DE_V_VEL,DE_H_VEL,DE_H_ENV, DE_H_ACC)"
                    "VALUES(%(Tag)s, %(Date)s, %(NDE-V-VEL)s, %(NDE-H-VEL)s, %(NDE-H-ENV)s, %(NDE-H-ACC)s, %(DE-V-VEL)s, %(DE-H-VEL)s, %(DE-H-ENV)s, %(DE-H-ACC)s)")
    
    cursor.execute(add_vibration_data,query)
    connection.commit()
    connection.close()
    return 0 # i have just inserted the return
    
def querying_data(tag,start_date,end_date,parameter):
    try:
        connection = mysql.connector.connect(host='localhost',
                             database='classicmodels',
                             user='root',
                             password='1807fidel'
                            )
        cursor=connection.cursor()
        query = 'SELECT {},{},{} FROM MOTOR1 WHERE DATE BETWEEN %s AND %s'.format('TAG','DATE','NDE_H_VEL')
        cursor.execute(query,(start_date,end_date))
        row = cursor.fetchall()
        
    except Error as e :
        print ("Error while connecting to MySQL", e)
    
    return row


def fft_plot(final_spectrum):
   
    layout = go.Layout(
        autosize = True,
        width = 600,
        height = 260,
        hovermode = 'closest',
        xaxis = dict(title = 'Frequency Spectrum'),
        yaxis=go.layout.YAxis(
        title='Y-axis Title',
        tickvals=[0, 0.5, 1, 1.5, 2, 2.5],
        automargin=True,
        titlefont=dict(size=10),
    ),
        margin=dict(l=30, r=4, b=4, t=40, pad=8),
        legend=dict(orientation="h"),
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    trace = go.Scatter(
        x = np.arange(0,len(final_spectrum)*7,7),
        y = final_spectrum,
        line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 1.5),
        name = 'spectrum {}'.format(final_spectrum)
        
    )
    
    return {"data": [trace], "layout": layout}
    
    
    
    
        
        
        
    
    
