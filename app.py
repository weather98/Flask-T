from flask import Flask
import sqlite3 as sql

with sql.connet("database.db") as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS question")
    cur.execute("CREATE TABLE question (id integer primary key, month integer, day interger, title text)")

app = Flask("board")

@app.route("/")
def index():
    return render_template("index.html") #templates 폴더의 index.html 을 렌더링

@app.route("/create", methods=['POST'])
def create():
    month = request.form['month']
    day = request.form['day']
    title = request.form['title']
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO question (month, day, title) VALUES (?, ?. ?)", (month, day, title))
    return redirect("/") #해당페이지로 다시 접속

app.run(host='127.0.0.1', port='5000')

