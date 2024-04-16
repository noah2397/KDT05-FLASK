# ===> main 범주의 url 라우팅을 views로 분리
# URL : /main, /main/info , /main/about ,........

from flask import Blueprint, render_template

# 블루프린트의 별칭, __name__, url_prefix
bp = Blueprint('root', __name__, url_prefix='/')

@bp.route('/')
def root():
    # html불러오기
    return render_template('main.html')

@bp.route('/result')
def result():
    # html불러오기
    return render_template('result.html')

