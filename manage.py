from flask_script import Manager, Server
from app import app
from app.models import Post
from app import db

manager = Manager(app)
manager.add_command("runserver",
                    Server(host="127.0.0.1", port=8000, use_debugger=True))

@manager.command
def save_post(author, title, content):
    post = Post(author=author,
        title=title,
        content=content)
    db.session.add(post)
    db.session.commit()

if __name__ == '__main__':
    manager.run()