from flask import *

app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def home():
   return render_template("main.html")

@app.route('/login')
def login():
   return render_template("login.html")

@app.route('/group')
def group():
   return render_template("group.html")



### 실행
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port='5000')