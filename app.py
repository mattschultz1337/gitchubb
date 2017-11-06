from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/learning-templates", methods=["GET", "POST"])
def learning_templates():
    if request.method == "POST":
        print(request.data)
        print(request.form)
    a = 2**7
    username = "steve"
    return render_template("learning_templates.html", answer=a, greeting=username)


if __name__ == "__main__":
	app.run(debug=True)