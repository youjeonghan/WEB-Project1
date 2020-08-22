import os
from flask import Flask, jsonify, request
from models import db, Board
from flask import redirect
from flask import render_template
from api import api
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(api, url_prefix='/api')

db.init_app(app)
db.app = app
db.create_all()		# db를 초기화 해줌

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/rooms')
def room():
	return render_template('Rooms.html')


if __name__ == "__main__":
	app.run(host='127.0.0.1',port=5000,debug=True)