from . import api
from flask import request
from flask import jsonify
from models import Fcuser, db
from flask_jwt import jwt_required

@api.route('/users', methods=['GET','POST'])#GET은 데이터에 대한 조회 POST는 생성
@jwt_required()#데코레이터로 로그인 사용자만 화면에 접근할 수 있게 하는 구문,이 구문이 있는 페이지에 들어가려면  Authorization에 토큰을 보내주어야한다.
def users():
    if request.method == 'POST':
        data = request.get_json()
        userid = data.get('userid')
        username = data.get('username')
        password = data.get('password')
        repassword = data.get('repassword')

        if not (userid and username and password and repassword):
            return jsonify({'error': 'No arguments'}), 400
        if password != repassword:
            return jsonify({'error':'Wrong password'}), 400
    
        fcuser = Fcuser()
        fcuser.userid = userid
        fcuser.username = username
        fcuser.password = password

        db.session.add(fcuser)
        db.session.commit()

        return  jsonify(), 201

    users = Fcuser.query.all()    # 모든 사용자에 대한 정보 가져오기
    # res_users = {}
    # for user in users:#반복문을 돌면서 직렬화된 변수를 넣어서 새로운 리스트를 만든다.
    #     res_users.append(user.serialize)
    # return jsonify(res_users)
    return jsonify([user.serialize for user in users])

@api.route('/users/<uid>', methods=['GET','PUT','DELETE'])
def user_detail(uid):
    if request.method == 'GET':
        user = Fcuser.query.filter(Fcuser.id == uid).first()
        return jsonify(user.serialize)
    elif request.method == 'DELETE':
        Fcuser.query.delete(Fcuesr.id == uid)
        return jsonify(), 204#204s는 상태 콜

    data = request.get_json()#POST형식에 경우 form형식으로 데이터를 전달하지만 api호출할 때처럼 json데이터를 전달할 때는 form에 데이터가 없으므로 다른 방식을 써야한다.

    userid = data.get('userid')
    username = data.get('username')
    password = data.get('password')

    updated_data = {}
    if userid:#userid가 있으면
        updated_data['userid'] = userid
    if username:
        updated_data['username'] = username
    if password:
        updated_data['password'] = password
  
    Fcuser.query.filter(Fcuser.id == uid).update(updated_data)#PUT은 전체를 업데이트할 때 사용하지만 일부 업데이트도 가능은함
    user = Fcuser.query.filter(Fcuser.id == uid).first()
    return jsonify(user.serialize)

