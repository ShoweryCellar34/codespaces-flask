from flask import Flask, render_template

app = Flask(__name__)

@app.route(route)
def hello_world():
    return render_template("index.html", title=route)
