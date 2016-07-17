from app import db
import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(80))
    title = db.Column(db.String(100))
    content = db.Column(db.Text())
    pub_date = db.Column(db.DateTime, default=datetime.datetime.now())

