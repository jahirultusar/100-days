from app import db


class HomeActivity(db.Model):
    """HomeActivity Model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    activity_date = db.Column(db.DateTime)
    activity_name = db.Column(db.String(128))
    activity_type = db.Column(db.String(128))
    duration_hour = db.Column(db.Float)

class Log(db.Model):
    """Log Model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    log_date = db.Column(db.DateTime)
    log_name = db.Column(db.String(128))
    log_type = db.Column(db.String(128))
    duration_hour = db.Column(db.Float)