#As we want to create models.py with SQLAlchemy for user and document data models.
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), unique=True)
    request_count = db.Column(db.Integer, default=0)

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    embedding = db.Column(db.PickleType, nullable=False)
#commit now.
