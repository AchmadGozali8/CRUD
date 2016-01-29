from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Polls(db.Model):
    __tablename__ = "polling"

    #fields
    id = db.Column(db.Integer, primary_key=True)
    nama_pemilih = db.Column(db.String(80))
    pilihan = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)

    def __inti__(self, nama_pemilih,pilihan,created_time):
        self.nama_pemilih = nama_pemilih
        self.pilihan = pilihan
    def __repr__(self):
        return '<Polls {}>'.format (self.nama_pemilih)
