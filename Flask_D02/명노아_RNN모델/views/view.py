from flask import Blueprint, render_template, request 
import sys, os, torch
import numpy as np
import pandas as pd
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from model.model import *

bp = Blueprint('data', __name__, template_folder = 'templates',
                    url_prefix="/")

@bp.route('/')
def input_data():
    return render_template('first.html', action='/display', method='POST')

@bp.route('/display', methods=['GET','POST'])
def save_post_data():
    req_dict = request.form.to_dict() # 데이터를 딕셔너리로 준다
    method = request.method # 데이터를 어떤 형식으로 받는지 알려줌
    if method == 'POST':
        req_dict = request.form.to_dict()
    output_count = req_dict.get('output_count')
    input_count = req_dict.get('input_count')
    
    df = pd.read_csv("명노아_RNN모델/static/test.csv")
    
    labels = list(df.index)[:int(output_count)]
    data1 = list(df['1'].values)[:int(output_count)]
    data2 = list(df['0'].values)[:int(output_count)]
    #return f"{labels}, {data1}, {data2}"
    return render_template('second.html', label=labels, data1=data1, data2=data2)