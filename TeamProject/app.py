import os
from flask import Flask, jsonify, request
<<<<<<< Updated upstream
from flask import redirect
from flask import render_template
from models import db, Board
from datetime import datetime

app = Flask(__name__)

@app.route('/insert')
def test():
	for i in range(1,3):     
		board = Board()
		board.subject = "이신필 병신 %d" % i
		board.content = "프론트 씨이발련아~ %d" % i
		board.create_date = datetime.now()

		db.session.add(board)
		db.session.commit()
	return "삽입 완료!!앙!"

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/rooms')
def room():
	return render_template('Rooms.html')
=======
# from models import db, Board
from flask import redirect
from flask import render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import config



app = Flask(__name__)
app.config.from_object(config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/flask_teamproject'
db = SQLAlchemy(app)


db.init_app(app)
db.app = app
db.create_all()

class Board(db.Model):				# 게시판 모델 : id,제목,내용,생성시간
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

@app.route('/insert')
def test():
    for i in range(1,3):     
        board = Board()
        board.subject = "이신필 병신 %d" % i
        board.content = "프론트 씨이발련아~ %d" % i
        board.create_date = datetime.now()

        db.session.add(board)
        db.session.commit()
    return "삽입 완료!!앙!"

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/rooms')
def room():
    return render_template('Rooms.html')
>>>>>>> Stashed changes


# 게시판 기능
# 나중에 api로 몰아넣을거임
@app.route('/board', methods=['GET','POST'])        # 게시판 목록 보여주기, 글쓰기
def board():
<<<<<<< Updated upstream
	if request.method == 'POST':									# 게시판 목록 추가	
		data = request.get_json()
		subject = data.get('subject')
		content = data.get('content')
		create_date = datetime.now()

		if not subject:
			return jsonify({'error': '제목이 없습니다.'}), 400

		if not content:
			return jsonify({'error': '내용이 없습니다.'}), 400

		board = Board()
		board.subject = subject
		board.content = content
		board.create_date = create_date

		db.session.add(board)
		db.session.commit()											# db에 저장

		return jsonify(), 201

	# GET
	boardlist = Board.query.all()
	return jsonify([board.serialize for board in boardlist])      # json으로 게시판 목록 리턴

@app.route('/board/<id>', methods=['GET','PUT','DELETE'])
def board_detail(id):
	if request.method == 'GET':									# 어떤id의 글
		board = Board.query.filter(Board.id == id).first()
		return jsonify(board.serialize)

	elif request.method == 'DELETE':							# 삭제
		Board.query.delete(Board.id == id)
		return jsonify(), 204		# 204는 no contents를 의미한다(앞으로 이용할수 없다는 뜻을 명시적으로알림, 성공을 알리는거긴함)

	data = request.get_json()
	Board.query.filter(Board.id == id).update(data)
	board = Board.query.filter(Board.id == id).first()
	return jsonify(board.serialize)								# 수정


basedir = os.path.abspath(os.path.dirname(__file__))
dbfile = os.path.join(basedir, 'db.sqlite')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + dbfile
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JSON_AS_ASCII'] = False

db.init_app(app)
db.app = app
db.create_all()
=======
    if request.method == 'POST':                                    # 게시판 목록 추가 
        data = request.get_json()
        subject = data.get('subject')
        content = data.get('content')
        create_date = datetime.now()

        if not subject:
            return jsonify({'error': '제목이 없습니다.'}), 400

        if not content:
            return jsonify({'error': '내용이 없습니다.'}), 400

        board = Board()
        board.subject = subject
        board.content = content
        board.create_date = create_date

        db.session.add(board)
        db.session.commit()                                         # db에 저장

        return jsonify(), 201

    # GET
    boardlist = Board.query.all()
    return jsonify([board.serialize for board in boardlist])      # json으로 게시판 목록 리턴

@app.route('/board/<id>', methods=['GET','PUT','DELETE'])
def board_detail(id):
    if request.method == 'GET':                                 # 어떤id의 글
        board = Board.query.filter(Board.id == id).first()
        return jsonify(board.serialize)

    elif request.method == 'DELETE':                            # 삭제
        Board.query.delete(Board.id == id)
        return jsonify(), 204       # 204는 no contents를 의미한다(앞으로 이용할수 없다는 뜻을 명시적으로알림, 성공을 알리는거긴함)

    data = request.get_json()
    Board.query.filter(Board.id == id).update(data)
    board = Board.query.filter(Board.id == id).first()
    return jsonify(board.serialize)                             # 수정




>>>>>>> Stashed changes

if __name__ == "__main__":
	app.run(host='127.0.0.1',port=5000,debug=True)