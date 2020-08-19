from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Board(db.Model):                                      # 게시판 모델 : id,제목,내용,생성시간
    __tablename__ = 'noticeboard'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'subject': self.subject,
            'content': self.content,
            'create_date': self.create_date
        }