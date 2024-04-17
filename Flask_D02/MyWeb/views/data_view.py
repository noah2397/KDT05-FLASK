# 역할 : 데이터 저장 및 출력관련 웹페이지 라우팅
# URL : /input
#       /input/save
#       /input/delete
#       /input/update
from flask import Blueprint, render_template, request 
import datetime
data_BP = Blueprint('data', __name__, template_folder = 'templates',
                    url_prefix="/input")

@data_BP.route('/')
def input_data():
    return render_template('input.html', action='/input/save',
                           method='POST')

@data_BP.route('/save', methods=['GET','POST'])
def save_post_data():
    req_dict = request.form.to_dict() # 데이터를 딕셔너리로 준다
    method = request.method # 데이터를 어떤 형식으로 받는지 알려줌
    if method == 'POST':
        req_dict = request.form.to_dict()
        image_file = request.files['filename'] # 이미지 갖고오기 
        image_filename = image_file.filename
        suffix=datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        image_file.save(f"MyWeb/static/img/{suffix}_{image_filename}")
        
        
        
    elif method == 'GET':
        req_dict = request.args.to_dict()
    headers  = request.headers # Request안에 들어있는 것들을 확인할 수 있다 
    #return f"SAVE POST DATA => {req_dict}<br>METHOD => {method}<br>HEADERS => {headers}<br>{image_file}<br>{image_filename}"
    return render_template('print_img.html', image_filename=f"../static/img/{suffix}_{image_filename}", sub_filename=f'img/{suffix}_{image_filename}')