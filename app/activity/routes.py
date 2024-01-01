import os
from datetime import datetime, date, timedelta
from flask import Blueprint, jsonify
from dotenv import load_dotenv
# from apscheduler.schedulers.background import BackgroundSchedulers
from sqlalchemy import func
from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectAuthenticationError,
    GarminConnectTooManyRequestsError,
)
from sqlalchemy.exc import SQLAlchemyError
from app import db
from app.activity.models import GarminData
# from sqlalchemy import func
# from run import app


# Load environment variables
load_dotenv()

# Create Blueprint
activity = Blueprint('activity', __name__)



def garmin_login():
    """Garmin Login with Garmin Connect."""
    email = os.getenv('GARMIN_EMAIL')
    password = os.getenv('GARMIN_PASSWORD')
    # Create Garmin client
    garmin_client = Garmin(email, password)
    try:
        # Authenticate with GarminConnect
        garmin_client.login()
    except (
        GarminConnectConnectionError,
        GarminConnectAuthenticationError,
        GarminConnectTooManyRequestsError,
    ) as err:
        # If there's an error, raise an exception
        return jsonify(f"Error occurred: {err}")

    # If the login is successful, return the client
    return garmin_client


def fetch_garmin_data():
    """Fetches data from Garmin."""
    try:
        # Create Garmin client
        garmin_client = garmin_login()

        # Fetch steps data
        today = date.today()

        # Fetch latest activities
        activities = garmin_client.get_activities(0, 1)
        if activities:
            active = activities[0]
            filtered_activity = {
                'activity_date': datetime.fromisoformat(active['startTimeLocal']),
                'activity_name': active['activityName'],
                'activity_type': active['activityType']['typeKey'],
                'duration_hour': round(active['duration'] / 3600, 2),  # Convert to hours and round off to 2 decimal places
                'distance_km': round(active['distance'] / 1000, 2),
            }

        # Fetch health stats
        health_stats = garmin_client.get_stats(today.isoformat())
        if health_stats:
            # consumed_calories = 0.00
            # if consumed_kilocalories is None:
            #     # consumed_kilocalories = health_stats.get('consumedKilocalories', 0.0)
            #     consumed_kilocalories = 0.00
            # else:
            #     consumed_kilocalories = health_stats['consumedKilocalories']
            filtered_health_stats = {
                'source': health_stats['source'],
                'date': datetime.fromisoformat(health_stats['calendarDate']),
                'last_sync': datetime.fromisoformat(health_stats['lastSyncTimestampGMT']),
                'daily_step_goal': health_stats['dailyStepGoal'],
                'total_steps': health_stats['totalSteps'],
                'net_calorie_goal': health_stats['netCalorieGoal'],
                'active_calories': health_stats['activeKilocalories'],
                'burned_calories': health_stats['bmrKilocalories'] + health_stats['activeKilocalories'],
                'consumed_calories': health_stats['consumedKilocalories'],
                # 'calorie_deficit': health_stats['netRemainingKilocalories'] - consumed_kilocalories,
                'calorie_deficit': int(health_stats['bmrKilocalories'] + health_stats['activeKilocalories']) - int(health_stats['consumedKilocalories']),
                'intensity_minutes_goal': health_stats['intensityMinutesGoal'],
                'active_minutes': round(health_stats['activeSeconds'] / 60), # Convert to minutes
                'average_stress_level': health_stats['averageStressLevel'],
                'body_battery': health_stats['bodyBatteryMostRecentValue'],
                'floor_climbed': round(health_stats['floorsAscended']),
                'max_heart_rate': health_stats['maxHeartRate'],
                'resting_heart_rate': health_stats['restingHeartRate'],
                'sleep_time': round(health_stats['sleepingSeconds'] / 3600, 2),

            }

        # Combine all data into one dictionary
        data = {
            'activity_data': filtered_activity,
            'health_stats': filtered_health_stats,
        }

        return data

    except (
        GarminConnectConnectionError,
        GarminConnectAuthenticationError,
        GarminConnectTooManyRequestsError,
    ) as err:
        return jsonify(f"No data found: {err}")



def save_garmin_data(data):
    """Saves data from Garmin to database."""
    # Create a new GarminData object
    garmin_data = GarminData(**data['activity_data'], **data['health_stats'])

    # Add the new GarminData object to the database session
    db.session.add(garmin_data)

    # Commit the session to save the GarminData object to the database
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error occurred: {e}")

def job():
    """Job to fetch and save Garmin data."""
    data = fetch_garmin_data()
    save_garmin_data(data)

# # Create a scheduler
# scheduler = BackgroundScheduler()

# # Schedule the job every 6 hours
# scheduler.add_job(job, 'interval', hours=2)

# # Start the scheduler
# scheduler.start()



# @activity.route('/api/stats', methods=['GET'])
# def get_stats():
#     """Returns the latest Garmin data."""
#         # Calculate the date 10 days ago
#     ten_days_ago = datetime.now() - timedelta(days=10)

#     # Query the database for all GarminData objects from the last 10 days
#     # data = GarminData.query.filter(GarminData.date >= ten_days_ago).all()
#     # data = (GarminData.query
#     #         .order_by(GarminData.last_sync).first()
#     #         .filter(GarminData.date >= ten_days_ago)
#     #         .all())
#     data = (db.session.query(GarminData)
#                 .group_by(GarminData.last_sync)
#                 .order_by((GarminData.date))
#                 .filter(GarminData.date >= ten_days_ago)
    #             .all())

    # # Convert the data to JSON
    # data_json = [datum.to_dict() for datum in data]

    # # Return the data as a JSON response
    # return jsonify(data_json)


@activity.route('/api/stats', methods=['GET'])
def get_stats():
    """Returns the latest Garmin data."""
    # Calculate the date 10 days ago
    ten_days_ago = datetime.now() - timedelta(days=10)

    # Subquery to find the latest timestamp for each day
    subquery = (db.session.query(func.date(GarminData.date).label('date'), func.max_(GarminData.last_sync).label('max_last_sync'))
                .group_by(func.date(GarminData.date))
                .filter(GarminData.date >= ten_days_ago)
                .subquery())

    # Query the database for the GarminData objects with the latest timestamp for each day
    data = (db.session.query(GarminData)
                .join(subquery, db.and_(func.date(GarminData.date) == subquery.c.date, GarminData.last_sync == subquery.c.max_last_sync))
                .all())

    # Convert the data to JSON
    data_json = [datum.to_dict() for datum in data]

    # Return the data as a JSON response
    return jsonify(data_json)

@activity.route('/api/fetch', methods=['GET'])
def fetch():
    job()
    return jsonify('Data fetched successfully!')