from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Fcuser(db.Model):
    __tablename = 'fcuser'
    id=db.Column(db.Integer, primary_key = True)
    password = db.Column(db.String(64))
    userid = db.Column(db.String(32))
    username = db.Column(db.String(8))

    #직렬화
    @property#실제로 함수로 만들지만 접근할 때는 변수처럼 사용할 수 있게 한다.
    def serialize(self):#serialize라는 변수
        return{
            'id': self.id,
            'password': self.password,
            'userid': self.userid,
            'username': self.username
        }