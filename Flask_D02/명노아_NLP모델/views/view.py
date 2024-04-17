from flask import Blueprint, render_template, request 
import datetime
import sys, os, torch
from PIL import Image
import numpy as np
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from model.NLP_MODEL import *

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
    
    MODEL = TextModel(5434, 64, 16, 4)
    MODEL.load_state_dict(torch.load("명노아_NLP모델/model/model_dict.pth"))
    return predict(MODEL, req_dict["text"])
    
    
    return f"{req_dict}"
  
    headers  = request.headers
    return render_template('second.html')