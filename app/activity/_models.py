from datetime import datetime
from app import db

class User(db.Model):
    """User"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email_address = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    steps = db.relationship('StepsData', backref='user', lazy=True)
    workouts = db.relationship('Activity', backref='user', lazy=True)
    strength = db.relationship('Strength', backref='user', lazy=True)
    runs = db.relationship('Run', backref='user', lazy=True)
    fasts = db.relationship('Fasting', backref='user', lazy=True)
    rests = db.relationship('Rest', backref='user', lazy=True)
    calories_in = db.relationship('CalorieIntake', backref='user', lazy=True)
    calories_out = db.relationship('CalorieBurn', backref='user', lazy=True)
    weight = db.relationship('Weight', backref='user', lazy=True)


class Activity(db.Model):
    """Daily workout model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    activity_name = db.Column(db.String(100), nullable=False)
    activity_type = db.Column(db.String(200), nullable=True)
    date_completed = db.Column(db.DateTime, default=datetime.utcnow)
    duration = db.Column(db.Integer, nullable=False)

# models.py
class StepsData(db.Model):
    """Steps data model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    steps = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)



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
    run_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date_completed = db.Column(db.Date, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    def get_duration_hours(self):
        """Return the duration in hours"""
        return self.duration // 60

    def get_duration_minutes(self):
        """Return the remaining duration in minutes after subtracting the hours"""
        return self.duration % 60

    distance = db.Column(db.Float, nullable=False)

class Fasting(db.Model):
    """Fasting day model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    duration = db.Column(db.Integer, nullable=False)

class Rest(db.Model):
    """Rest day model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date_completed = db.Column(db.DateTime, default=datetime.utcnow)

class CalorieIntake(db.Model):
    """Calorie intake model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    calories_in = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

class CalorieBurn(db.Model):
    """Calorie burn model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    calories_out = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


class Weight(db.Model):
    """Weight model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

