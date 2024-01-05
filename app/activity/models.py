from app import db
from datetime import datetime

class User(db.Model):
    """User Model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email_address = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

class GarminData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Activity data fields
    activity_date = db.Column(db.DateTime)
    activity_name = db.Column(db.String(128))
    activity_type = db.Column(db.String(128))
    duration_hour = db.Column(db.Float)
    distance_km = db.Column(db.Float)

    # Health stats fields
    source = db.Column(db.String(128))
    date = db.Column(db.Date)
    last_sync = db.Column(db.DateTime)
    daily_step_goal = db.Column(db.Integer)
    total_steps = db.Column(db.Integer)
    net_calorie_goal = db.Column(db.Float)
    active_calories = db.Column(db.Float)
    burned_calories = db.Column(db.Float)
    consumed_calories = db.Column(db.Float)
    calorie_deficit = db.Column(db.Float)
    intensity_minutes_goal = db.Column(db.Integer)
    active_minutes = db.Column(db.Float)
    average_stress_level = db.Column(db.Integer)
    body_battery = db.Column(db.Integer)
    floor_climbed = db.Column(db.Float)
    max_heart_rate = db.Column(db.Integer)
    resting_heart_rate = db.Column(db.Integer)
    sleep_time = db.Column(db.Float)
    last_created = db.Column(db.DateTime, default=datetime.utcnow)


    def to_dict(self):
        return {
            'activity_data': {
                'activity_date': self.activity_date,
                'activity_name': self.activity_name,
                'activity_type': self.activity_type,
                'duration_hour': self.duration_hour,
                'distance_km': self.distance_km,
            },
            'health_stats': {
                'source': self.source,
                'date': self.date,
                'last_sync': self.last_sync,
                'daily_step_goall': self.daily_step_goal,
                'total_steps': int(self.total_steps),
                'net_calorie_goal': self.net_calorie_goal,
                'active_calories': self.active_calories,
                'burned_calories': self.burned_calories,
                'consumed_calories': self.consumed_calories,
                'calorie_deficit': self.calorie_deficit,
                'intensity_minutes_goal': self.intensity_minutes_goal,
                'active_minutes': self.active_minutes,
                'average_stress_level': self.average_stress_level,
                'body_battery': int(self.body_battery),
                'floor_climbed': self.floor_climbed,
                'max_heart_rate': self.max_heart_rate,
                'resting_heart_rate': self.resting_heart_rate,
                'sleep_time': self.sleep_time,
                # 'last_created': self.last_created,
            },
        }