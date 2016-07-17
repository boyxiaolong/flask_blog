from app import app
from flask import render_template
from .models import Post

@app.route('/')
def index():
    return render_template('welcome.html', title='welcome')

@app.route('/home')
def home():
    posts = Post.query.all()
    return render_template('post.html', title="Home", posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.query.filter_by(id=post_id).first()
    return render_template('post_detail.html', post=post)

@app.route('/aboutme')
def about():
    return render_template('aboutme.html')

@app.route('/archive')
def archive():
    print('archive')
    posts = Post.query.all()
    return render_template('archive.html', posts=posts)