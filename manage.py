from flask_script import Manager, Server
from app import app
from app.models import Post
from app import db
from flask_script.commands import ShowUrls
from flask_migrate import MigrateCommand

manager = Manager(app)
manager.add_command("runserver",
                    Server(host="127.0.0.1", port=8000, use_debugger=True))
manager.add_command('showurls', ShowUrls())
manager.add_command('db', MigrateCommand)
@manager.command
def save_post(author, title, content):
    post = Post(author=author,
        title=title,
        content=content)
    db.session.add(post)
    db.session.commit()

@manager.command
def query_titles():
    posts = Post.query.all()
    for post in posts:
        print(post.id, post)

@manager.command
def modify_post(title, content):
    post = Post.query.filter_by(title=title).first()
    if post is None:
        print('not find title:%s in db' % title)
    else:
        post.content = content
        db.session.add(post)
        db.session.commit()
        print('modify post titie:%s with content:%s' % (title, content))

@manager.command
def del_post(id):
    id = int(id)
    post = Post.query.get(id)
    if post is None:
        print('not find id:%d in db' % id)
    else:
        db.session.delete(post)
        db.session.commit()
        print('del post id:%d' % (id))

@manager.command
def create_table():
    db.create_all()

@manager.command
def drop_table():
    db.drop_all()

if __name__ == '__main__':
    manager.run()