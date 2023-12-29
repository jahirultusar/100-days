from app import db

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
    net_calorie_goal = db.Column(db.Integer)
    active_calories = db.Column(db.Integer)
    burned_calories = db.Column(db.Integer)
    consumed_calories = db.Column(db.Integer)
    calorie_deficit = db.Column(db.Integer)
    intensity_minutes_goal = db.Column(db.Integer)
    active_minutes = db.Column(db.Float)
    average_stress_level = db.Column(db.Integer)
    body_battery = db.Column(db.Integer)
    floor_climbed = db.Column(db.Float)
    max_heart_rate = db.Column(db.Integer)
    resting_heart_rate = db.Column(db.Integer)
    sleep_time = db.Column(db.Float)


    def to_dict(self):
        return {
            'activity_data': {
                'Activity Date': self.activity_date,
                'Activity Name': self.activity_name,
                'Activity Type': self.activity_type,
                'Duration (h)': self.duration_hour,
                'Distance (km)': self.distance_km,
            },
            'health_stats': {
                'Source': self.source,
                'Date': self.date,
                'Last Sync': self.last_sync,
                'Daily Step Goal': self.daily_step_goal,
                'Total Steps': self.total_steps,
                'Net Calories Goal': self.net_calorie_goal,
                'Active Calories': self.active_calories,
                'Burned Calories': self.burned_calories,
                'Consumed Calories': self.consumed_calories,
                'Calorie Deficit': self.calorie_deficit,
                'Intensity Minutes Goal': self.intensity_minutes_goal,
                'Active Minutes': self.active_minutes,
                'Average Stress Level': self.average_stress_level,
                'Body Battery': self.body_battery,
                'Floor Climbed': self.floor_climbed,
                'Max Heart Rate': self.max_heart_rate,
                'Resting Heart Rate': self.resting_heart_rate,
                'Sleeping Time': self.sleep_time,
            },
        }