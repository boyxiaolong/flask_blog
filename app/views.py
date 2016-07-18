from app import app
from flask import render_template,request
from .models import Post,UserInfo
from flask.views import MethodView
from .forms import UserRegisterForm

@app.route('/')
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

class LoginRequestView(MethodView):
    def get(self):
        return render_template('login.html', form=UserRegisterForm())

    def post(self):
        print('post')
        form = UserRegisterForm(request.form)
        if form.validate():
            username = form.username.data
            pwd = form.password.data
            print(username, pwd)
            user = UserInfo.query.filter_by(username=username).first()

app.add_url_rule('/login', view_func=LoginRequestView.as_view('login'))