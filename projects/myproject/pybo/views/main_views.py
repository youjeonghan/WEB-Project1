# 모든 기능을 main_views.py에 구현할 수도 있겠지만 기능별로 블루프린트 파일로 분리하여 관리

from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')        # 이름, 모듈명, URL 프리픽스 값 (__name__ => 현재 모듈이름)


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))