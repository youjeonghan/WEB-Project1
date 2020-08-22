from flask import jsonify
from flask import request
from models import Board, db
from datetime import datetime
from . import api

# 게시판 기능
@api.route('/board', methods=['GET','POST'])            # 게시판 목록 보여주기, 글쓰기
def board():
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

@api.route('/board/<id>', methods=['GET','PUT','DELETE'])
def board_detail(id):
    if request.method == 'GET':                                 # 어떤id의 글
        board = Board.query.filter(Board.id == id).first()
        return jsonify(board.serialize)

    elif request.method == 'DELETE':                            # 삭제
        board = Board.query.filter(Board.id == id).first()
        db.session.delete(board)
        db.session.commit()
        return jsonify(), 204       # 204는 no contents를 의미한다(앞으로 이용할수 없다는 뜻을 명시적으로알림, 성공을 알리는거긴함)

    data = request.get_json()
    Board.query.filter(Board.id == id).update(data)
    board = Board.query.filter(Board.id == id).first()
    return jsonify(board.serialize)                             # 수정