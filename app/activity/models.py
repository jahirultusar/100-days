from datetime import datetime
from app import db

class User(db.Model):
    """User"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email_address = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    workouts = db.relationship('Workout', backref='user', lazy=True)
    strength = db.relationship('Strength', backref='user', lazy=True)
    runs = db.relationship('Run', backref='user', lazy=True)
    fasts = db.relationship('Fasting', backref='user', lazy=True)
    rests = db.relationship('Rest', backref='user', lazy=True)

class Workout(db.Model):
    """Daily workout model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date_completed = db.Column(db.DateTime, default=datetime.utcnow)
    duration = db.Column(db.Integer, nullable=False)

class Strength(db.Model):
    """Strength workout model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date_completed = db.Column(db.DateTime, default=datetime.utcnow)
    duration = db.Column(db.Integer, nullable=False)

class Run(db.Model):
    """Run model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date_completed = db.Column(db.DateTime, default=datetime.utcnow)
    duration = db.Column(db.Integer, nullable=False)
    distance = db.Column(db.Float, nullable=False)
    run_type = db.Column(db.String(100), nullable=False)

class Fasting(db.Model):
    """Fasting day model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date_completed = db.Column(db.DateTime, default=datetime.utcnow)
    duration = db.Column(db.Integer, nullable=False)

class Rest(db.Model):
    """Rest day model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date_completed = db.Column(db.DateTime, default=datetime.utcnow)



