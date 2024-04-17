# 역할 : 데이터 저장 및 출력관련 웹페이지 라우팅
# URL : /input
#       /input/save
#       /input/delete
#       /input/update
from flask import Blueprint, render_template, request 

data_BP = Blueprint('data', __name__, template_folder = 'templates',
                    url_prefix="/input")

@data_BP.route('/')
def input_data():
    return render_template("input.html")

@data_BP.route('/save_get')
def save_get_data():
    request.args.get('value')
    request.args.get('message')
    return "SAVE GET DATA"

@data_BP.route('/save_post')
def save_post_data():
    return "SAVE POST DATA"



