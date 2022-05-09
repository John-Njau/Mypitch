from datetime import datetime

from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from . import db, login_manager

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password_hashed = db.Column(db.String(128))
    # pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))

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


class Pitch(db.Model):
    __tablename__ = 'pitch'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    pitchtext = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # user = db.relationship('User', backref='pitch', lazy='dynamic')
    comment = db.relationship('Comment', backref='pitch', lazy='dynamic')
    upvotes = db.relationship('Upvote', backref='pitch', lazy='dynamic')
    downvotes = db.relationship('Downvote', backref='pitch', lazy='dynamic')

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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_comment(self):
        db.session.add(self)
        db.session.commit()

class Upvote(db.Model):
    __tablename__ = 'upvotes'
    
    id = db.Column(db.Integer, primary_key=True)
    upvotes = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))

    
    def save_upvote(self):
        db.session.add(self)
        db.session.commit()
        
    def upvote(self, id):
        upvote_pitch = Upvote(user=current_user, pitch_id=id)
        upvote_pitch.save_upvote()
        
    @classmethod
    def get_upvote(cls, id):
        upvote = Upvote.query.filter_by(pitch_id=id).all()
        return upvote
    
    @classmethod
    def all_upvotes(cls):
        upvotes = Upvote.query.order_by('id').all()
        return upvotes
        
class Downvote(db.Model):
    __tablename__ = 'downvotes'
    
    id = db.Column(db.Integer, primary_key=True)
    downvotes = db.Column(db.Integer,default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'))
    
    def save_downvote(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_downvote(self):
        db.session.add(self)
        db.session.commit()
    
    def downvote(self, id):
        downvote_pitch = Downvote(user=current_user, pitch_id=id)
        downvote_pitch.save_downvote()
        
    @classmethod
    def get_downvote(cls, id):
        downvote = Downvote.query.filter_by(pitch_id=id).all()
        return downvote
    
    @classmethod
    def all_downvotes(cls):
        downvotes = Downvote.query.order_by('id').all()
        return downvotes
        