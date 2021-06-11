import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')#os.urandom(24)
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///dbapi.db' ## os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False