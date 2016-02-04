from flask import Flask, render_template,request,redirect
from models import db, Polls
import datetime
app = Flask(__name__)
app.config.from_object("config")
db.init_app(app)



@app.route("/")
def awal():

    return render_template('index.html')
#menampilkan semua data di dalam table
@app.route("/polls")
def all():
    polls=Polls.query.all()

    return render_template('data_user.html',**locals())

#menampilkan data berdasarkan id
@app.route("/polls/<int:id>")
def filter(id):
    polls = Polls.query.get(id)

    return render_template('user.html',**locals())

#menambahkan data ke dalam table
@app.route("/polls/add",methods=["POST","GET"])
def add():
    if request.method=="POST":
        nama_pemilih = request.form.get("name",None)
        pilihan = request.form.get("pilihan",None)

        polls = Polls(nama_pemilih,pilihan)
        polls.created_time=datetime.datetime.now()
        db.session.add(polls)
        db.session.commit()
        return redirect('/polls')
    return render_template("add_user.html",**locals())
#mengupdate ke dalam table
@app.route("/polls/update/<int:id>",methods=["POST","GET"])
def update(id):
    if request.method == "POST":
        pilihan_baru = request.form.get("pilihan",None)
        polls = Polls.query.get(id)
        polls.pilihan = pilihan_baru
        db.session.add(polls)
        db.session.commit()
        return redirect('/polls')
    polls=Polls.query.get(id)
    return render_template("update.html", **locals())
#menghapus data dalam database
@app.route("/polls/delete/<int:id>")
def delete(id):
    polls = Polls.query.get(id)
    db.session.delete(polls)
    db.session.commit()

    return redirect("/polls")

if  __name__ =="__main__":
    app.run(debug=True)
