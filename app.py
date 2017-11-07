from flask import Flask, render_template, request
import time

app = Flask(__name__)
app.run(host='0.0.0.0')

@app.route("/")
def index():
	x = int(round(time.time() * 1000))
	return render_template("index.html", stylevar=x)

if __name__ == "__main__":
	app.run(debug=True)
