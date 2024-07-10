from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum as SQLAlchemyEnum
from datetime import datetime
from enum import Enum

db = SQLAlchemy()

class UserRole(Enum):
    ADMIN = 'admin'


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(50), unique = True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(70), unique = True)
    password = db.Column(db.String(250))
    role = db.Column(SQLAlchemyEnum(UserRole), default=UserRole.ADMIN)
    def to_dict(self):
        return {
            'id': self.public_id,
            'name': self.name,
            'username': self.username,
        }

class Device(db.Model):
    __tablename__ = 'devices'
    idQR = db.Column(db.String(45), primary_key = True)
    idLnms = db.Column(db.String(45))
    name = db.Column(db.String(45))
    updated_on = db.Column(db.DateTime, default=datetime.utcnow)
    data = db.Column(db.Text)       
