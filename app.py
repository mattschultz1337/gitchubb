from flask import Flask, render_template, request
import time
import os


app = Flask(__name__)

@app.route("/")
def index():
	x = int(round(time.time() * 1000))
	return render_template("index.html", stylevar=x)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port="33", debug=True)
