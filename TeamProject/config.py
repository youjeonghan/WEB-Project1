import os

# basedir = os.path.abspath(os.path.dirname(__file__))
# dbfile = os.path.join(basedir, 'db.sqlite')

# SQLALCHEMY_DATABASE_URI = "sqlite:///" + dbfile
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_AS_ASCII = False