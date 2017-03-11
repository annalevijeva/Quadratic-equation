from flask import Flask, render_template, request
from equation import solve

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/", methods=['POST', 'GET'])
def form_post():
    if request.method == "POST":
        a = request.form['a']
        b = request.form['b']
        c = request.form['c']
        result = solve([a, b, c])
        return render_template("success.html", result=result)
    else:
        render_template("index.html")


if __name__ == "__main__":
    app.run()
