#!/usr/bin/env python3
import base64
import datetime
import io
import os
from collections import defaultdict

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import plotly.graph_objs as go
from plotly.subplots import make_subplots

import numpy as np
import soundfile as sf
import librosa as lb
import scipy.signal as sig

from flask import Flask, render_template

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = Flask(__name__)
app = dash.Dash(name='app1', sharing=True, server=server, csrf_protect=False, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.H5('Spectrogram Viewer'),
        # File upload bunner
        dcc.Upload(
            id='upload-data',
            children=html.Div(['Drag and Drop or ',
                               html.A('Select Files')]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            # Allow multiple files to be uploaded
            multiple=True),
        # File Information
        html.Div(id='the_graph'),
        # Graph
        html.Div(id='output-data-upload'),
        html.P('[Option]'),
        html.Div([
        	html.P('* Time-scale'),
        	dcc.RadioItems(id='xaxis-type',
                       options=[{
                           'label': i,
                           'value': i
                       } for i in ['sec', 'sample']],
                       value='sec',
                       labelStyle={'display': 'inline'}),
        ]),
        html.Div([
        	html.P('* Frequency-scale'),
        	dcc.RadioItems(id='yaxis-type',
                       options=[{
                           'label': i,
                           'value': i
                       } for i in ['linear', 'log']],
                       value='linear',
                       labelStyle={'display': 'inline'}),
        ]),
    ], )
        
        
def spectrogram(df, fs, nframe=1024):

    noverlap = np.round(nframe*0.9).astype(int)
    f, t, spec = sig.spectrogram(df, fs=fs, window='blackmanharris',
                                 nperseg=nframe, noverlap=noverlap)

    return f, t, spec


def spectrogram_plot(
        df,
        fs,
        spec,
        t,
        f,
        filename,
        xaxis_type,
        yaxis_type,
):
    """アップロードされたデータのグラフを描画"""
    # ラジオボタンでx軸の表示尺度を変更
    if xaxis_type == 'sec':
        x_ind = np.arange(df.shape[0])/fs
        x_ind2 = t-t[1]
        x_title = 'Time [s]'
    else:
        x_ind = np.arange(df.shape[0])
        x_ind2 = (t-t[1])*fs
        x_title = 'Samples'

    if yaxis_type == 'log':
        y = f
        y_title = "Frequency"
        y_range = [1, np.log10(np.max(y))]
        x_range = [x_ind2[1], x_ind2[-2]]
    else:
        y = f / 1000
        y_title = "Frequency [kHz]"
        y_range = [0, np.max(y)]
        x_range = [x_ind2[1], x_ind2[-2]]

    # 図
    spec_data = go.Heatmap(z=spec,x=x_ind2,y=y, colorscale='Electric',
                           zmin=np.max(spec), zmax=np.min(spec), showscale=False)
    wave_data = go.Scatter(x=x_ind, y=df, mode='lines', xaxis="x", yaxis="y2")
    data = [spec_data, wave_data]
    
    # グラフのレイアウト

    height = 500
    xaxis  = dict(title_text=x_title, range=x_range)
    yaxis  = dict(title_text=y_title, domain = [0,0.8], range=y_range)
    yaxis2 = dict(title_text="Amplitude", domain = [0.85,1])
    layout = go.Layout(xaxis=xaxis, yaxis=yaxis, yaxis2=yaxis2, yaxis_type=yaxis_type,
             height = height, showlegend=False, autosize=True, margin=dict(l=10, r=10, t=20, b=10))

    return dcc.Graph(id='the_graph', figure=go.Figure(data=data, layout=layout))

def parse_contents(contents, filename, date, xaxis_type,
                   yaxis_type):
    content_type, content_string = contents.split(',')
	
    decoded = base64.b64decode(content_string)
    try:
        if 'wav' in filename:
            # Assume that the user uploaded a wav file
            df, fs = sf.read(io.BytesIO(decoded))

        elif 'mp3' in filename:
            # Assume that the user uploaded a wav file
            df, fs = sf.read(io.BytesIO(decoded))

    except Exception as e:
        print(e)
        return html.Div(['There was an error processing this file.'])

    f, t, spec = spectrogram(df, fs=fs)
    spec = 2*np.log10(spec+10**(-10))

    return html.Div([
    	html.P('Name :  "{0}"    [ Sampling Frequency : {1} Hz ]'.format(filename, fs)),
        spectrogram_plot(df, fs, spec, t, f, filename, xaxis_type, yaxis_type),
        html.Hr()  # horizontal line
    ])


@app.callback(Output(
    'output-data-upload',
    'children',
), [
    Input('upload-data', 'contents'),
    Input('xaxis-type', 'value'),
    Input('yaxis-type', 'value'),
], [State('upload-data', 'filename'),
    State('upload-data', 'last_modified')])
def update_output(list_of_contents, xaxis_type, yaxis_type,
                  list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d, xaxis_type, yaxis_type)
            for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)
        ]
        return children


if __name__ == '__main__':
    app.run_server(debug=True, port=8880)