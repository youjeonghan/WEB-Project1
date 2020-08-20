from flask import *
from flask import Flask, render_template

app = Flask(__name__, instance_relative_config=True)

@app.route('/')
def home():
   return render_template("index.html")

### 실행
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port='5000')