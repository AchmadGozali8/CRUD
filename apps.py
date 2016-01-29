from flask import Flask, render_template
from models import db, Polls

app = Flask(__name__)
app.config.from_object("config")
db.init_app(app)


#menampilkan semua data di dalam table
@app.route("/polls")
def all():
    allpolls=Polls.query.all()

    return render_template('index.html')

#menampilkan data berdasarkan id
@app.route("/polls/:id")
def filter(id):
    id_filter = Polls.query.get(id)

    return render_template('index.html')

if  __name__ =="__main__":
    app.run(debug=True)
