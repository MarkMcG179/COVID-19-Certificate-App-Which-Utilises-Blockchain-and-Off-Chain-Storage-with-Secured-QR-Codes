from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    accountNum = db.Column(db.Integer, unique=True)
    password = db.Column(db.String, nullable=False)

class Cert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(), nullable=False)
    lastName = db.Column(db.String(), nullable=False)
    DOB = db.Column(db.DATE, nullable=False)
    status = db.Column(db.String(), nullable=False)
    country = db.Column(db.String(), nullable=False)
    manufacturer = db.Column(db.String(), nullable=False)
    vaccinationDate = db.Column(db.DATE, nullable=False)
    certIssuer = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

def __repr__(self):
    return 'Name %r' % self.id