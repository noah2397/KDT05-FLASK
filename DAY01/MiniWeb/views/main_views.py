# ===> main 범주의 url 라우팅을 views로 분리
# URL : /main, /main/info , /main/about ,........

from flask import Blueprint

# 블루프린트의 별칭, __name__, url_prefix
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return 'main index'

