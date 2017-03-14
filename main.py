from flask import Flask, render_template, request, session
from equation import solve
from save_graph import save_png
import os
import time

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=['POST', 'GET'])
def form_post():
    try:
        os.remove("static/images/g.png")
    except FileNotFoundError:
        pass
    if request.method == "POST":
        a = request.form['a']
        b = request.form['b']
        c = request.form['c']
        result = solve([a, b, c])
        if isinstance(result, list):
            save_png(a, b, c)
        unixtime = time.time()
        return render_template("success.html", result=result, unixtime=unixtime)
    else:
        render_template("index.html")


if __name__ == "__main__":
    app.run()
