import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + BASE_DIR + '/test.db'

SECRET_KEY = 'super secret key'
SESSION_TYPE = 'filesystem'
SQLALCHEMY_TRACK_MODIFICATIONS = True