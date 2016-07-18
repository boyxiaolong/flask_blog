from app import db
import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(80))
    title = db.Column(db.String(100), unique=True)
    content = db.Column(db.Text())
    pub_date = db.Column(db.DateTime, default=datetime.datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))

    def __str__(self):
        return '%s' % self.title

class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    posts = db.relationship('Post', backref='userinfo')

    def __str__(self):
        return '%s' % self.username
