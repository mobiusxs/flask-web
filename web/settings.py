from os import environ

SQLALCHEMY_DATABASE_URI = environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False
