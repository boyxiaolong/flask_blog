from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app)

from app import views, models


admin.add_view(ModelView(models.Post, db.session))
admin.add_view(ModelView(models.UserInfo, db.session))