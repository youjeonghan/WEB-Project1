import os
BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))  # 'BASE_DIR/pybo.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False      # SQLALCHEMY_TRACK_MODIFICATIONS는 SQLAlchemy의 이벤트들을 처리하기 위한 옵션

