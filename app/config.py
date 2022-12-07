import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
# C:\Users\angel\Desktop\Flask-blog\app\config.py


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'lskd934ja2mdi24mai'
    SECURITY_PASSWORD_SALT='asdf4a5sd'
    SECURITY_PASSWORD_HASH='sha512_crypt'
