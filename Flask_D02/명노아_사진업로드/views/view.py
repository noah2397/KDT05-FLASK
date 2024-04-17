from flask import Blueprint, render_template, request 
import datetime

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
        image_file = request.files['filename'] # 이미지 갖고오기 
        image_filename = image_file.filename
        suffix=datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        image_file.save(f"명노아_사진업로드/static/img/{suffix}_{image_filename}")
  
    headers  = request.headers
    return render_template('second.html', image_filename=f"../static/img/{suffix}_{image_filename}", sub_filename=f'img/{suffix}_{image_filename}')