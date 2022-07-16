from flask import Flask, render_template, request, redirect
import sqlite3 as sql

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("Home.html")


@app.route("/about")
def about():
    return render_template("About.html")


@app.route("/conlangs")
def conlang():
    return render_template("Conlangs.html")


@app.route("/tips")
def tips():
    return render_template("Tips.html")


@app.route("/words")
def words():
    return render_template("words.html")


@app.route("/phonetics")
def phonetics():
    return render_template("Phonetics.html")


@app.route("/orthography")
def ortho():
    return render_template("Orthography.html")


@app.route("/blog")
def blog():
    return render_template("Blog.html")


@app.route("/blog/poem")
def post1():
    return render_template("post1.html")


@app.route("/contact")
def contact():
    return render_template("Contact.html")


@app.route("/join")
def join():
    return render_template("Join.html")


@app.route('/apply', methods=['POST', 'GET'])
def apply():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            email = request.form['email']
            mesg = request.form['mess']
            ty = "application"

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO contacts (name,email,msg,type) VALUES(?, ?, ?, ?)", (nm, email, mesg, ty))

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("Home.html")
            con.close()


@app.route('/sub', methods=['POST', 'GET'])
def sub():
    if request.method == 'POST':
        try:
            email = request.form['emaila']
            nm = request.form['namea']
            ty = "mailList"
            mesg = ""

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO contacts (name,email,msg,type) VALUES(?, ?, ?, ?)", (nm, email, mesg, ty))

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("Home.html")
            con.close()


@app.route('/msg', methods=['POST', 'GET'])
def msg():
    if request.method == 'POST':
        try:
            email = request.form['emailb']
            nm = request.form['nameb']
            ty = "message"
            mesg = request.form['msgLong']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO contacts (name,email,msg,type) VALUES(?, ?, ?, ?)", (nm, email, mesg, ty))

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("Home.html")
            con.close()


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from contacts")

    rows = cur.fetchall();
    return render_template("list.html", rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
