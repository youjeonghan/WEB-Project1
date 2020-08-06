from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()     # 데이터베이스를 직접 수정하는 대신 모델을 통해 데이터베이스를 변경할 수 있도록 도와주는 라이브러리

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)      # config.py에 작성한 항목들을 app.config 환경변수로 읽어들이기 위한 문장

    # ORM: 개발자가 직접 쿼리문을 작성하지 않고 테이블과 매핑된 모델 객체를 통해서 데이터 작업을 처리하는 방식
    # db 객체를 create_app 함수내에서 생성하면 블루프린트와 같은 다른 모듈에서 db객체를 import하여 사용할수 없기 때문에
    # 이처럼 create_app 함수 밖에서 생성하고 실제 객체 초기화는 create_app에서 수행하는 패턴
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    # 블루프린트
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app