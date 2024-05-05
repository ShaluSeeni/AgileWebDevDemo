import os

basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

    #SQLALCHEMY_DATABASE_URI = os.path( basedir, 'app.db')
    SQLALCHEMY_TRACK_NOTIFICATIONS = False