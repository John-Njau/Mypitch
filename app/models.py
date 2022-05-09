from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db, login_manager

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password_hashed = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    
    @password.setter
    def password(self, password):
        self.password_hashed = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hashed, password)
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()


class Pitch(UserMixin, db.Model):
    __tablename__ = 'pitch'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    pitchtext = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(255), nullable=False)
    comment = db.relationship('Comment', backref='pitch', lazy='dynamic')
    upvotes = db.relationship('UpVote', backref='pitch', lazy='dynamic')
    downvotes = db.relationship('DownVote', backref='pitch', lazy='dynamic')

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def delete_pitch(self):
        db.session.delete(self)
        db.session.commit()

class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    commenttext = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'), nullable=False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_comment(self):
        db.session.add(self)
        db.session.commit()

class Upvotes(db.Model):
    __tablename__ = 'upvotes'
    
    id = db.Column(db.Integer, primary_key=True)
    upvotes = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    
    def save_upvotes(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_upvotes(self):
        db.session.delete(self)
        db.session.commit()
        
class Downvotes(db.Model):
    __tablename__ = 'downvotes'
    
    id = db.Column(db.Integer, primary_key=True)
    downvotes = db.Column(db.Integer,default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    
    def save_downvotes(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_downvotes(self):
        db.session.add(self)
        db.session.commit()