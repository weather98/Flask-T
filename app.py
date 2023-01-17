from flask import Flask

app = Flask("board")

@app.route("/")
def index():
    return "<h1>hello flask</h1>"

app.run(host='127.0.0.1', port='5000')