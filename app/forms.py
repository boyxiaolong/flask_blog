from flask_wtf import Form
from wtforms import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired, Email

class UserRegisterForm(Form):
    username = StringField('username')
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Submit')