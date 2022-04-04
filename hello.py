from flask import Flask

app = Flask('oie')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"