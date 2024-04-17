from flask import Blueprint, render_template, request 
import datetime
import sys, os, torch
from PIL import Image
import numpy as np
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from model.CNN_MODEL import *
import torch.nn as nn
import torch.nn.functional as F
import cv2
import torch

bp = Blueprint('data', __name__, template_folder = 'templates',
                    url_prefix="/")

@bp.route('/')
def input_data():
    return render_template('first.html', action='/display', method='POST')

@bp.route('/display', methods=['GET','POST'])
def save_post_data():
    method = request.method
    if method == 'POST':
        image_file = request.files['filename'] # 이미지 갖고오기 
        image_filename = image_file.filename
        suffix=datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        image_file.save(f"명노아_CNN모델/static/img/{suffix}_{image_filename}")
    global model
    model = CNN()
    model.load_state_dict(torch.load("명노아_CNN모델/model/Bekki.pth"))
    
    # 이미지 읽기
    img = Image.open(f"명노아_CNN모델/static/img/{suffix}_{image_filename}")
    img = img.resize((50, 50))  # 이미지 resize
    
    # Pillow 이미지를 numpy 배열로 변환
    img_np = np.array(img)

    # 이미지 확인 (선택 사항)
    img.show()

    # 모델에 입력하기 위해 이미지 형태 변경
    img_tensor = torch.FloatTensor(img_np.transpose((2, 0, 1)))  # 이미지 채널 변환 및 텐서로 변환
    img_tensor = img_tensor.unsqueeze(0)  # 배치 차원 추가

    # 모델 예측 코드 작성
    if not model(img_tensor).argmax():
        result = "Anya~"
    else: 
        result = "Bekki~"    
    
    return render_template('second.html', image_filename=f"../static/img/{suffix}_{image_filename}", sub_filename=f'img/{suffix}_{image_filename}', result=result)