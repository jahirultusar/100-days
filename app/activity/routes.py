import os
import csv
from flask import Blueprint, jsonify, current_app
from dotenv import load_dotenv

from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectAuthenticationError,
    GarminConnectTooManyRequestsError,
)

# Load environment variables

from app.activity.models import StepsData, HeartRateData
load_dotenv()


# User, Workout, Strength, Run, Fasting, Rest, CalorieIntake, CalorieBurn, CalorieDeficit, Weight,

activity = Blueprint('activity', __name__)


############## Api Starts Here ##############
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


@activity.route('/api/activity', methods=['GET'])
def fetch_garmin_activities():
    """Fetches steps data from Garmin Connect API."""
    try:
        # Create Garmin client
        garmin_client = garmin_login()

        # Fetch activities
        activities = garmin_client.get_activities(0, 1)  # Fetch the latest activity

        # Print details of the first activity
        if activities:
            first_activity = activities[0]  # Rename the variable 'activity' to 'first_activity'
            filtered_activity = {
                'Activity Name': first_activity['activityName'],
                'Activity Type': first_activity['activityType']['typeKey'],
                'Duration (s)': first_activity['duration'],
                'Distance (m)': first_activity['distance'],
            }
            return jsonify(filtered_activity)

    except (
        GarminConnectConnectionError,
        GarminConnectAuthenticationError,
        GarminConnectTooManyRequestsError,
    ) as err:
        return jsonify(f"No activities found: {err}")

@activity.route('/api/stepsData', methods=['GET'])
def fetch_steps_from_csv():
    """Fetches steps data from a CSV file."""
    try:
        # Open the CSV file
        file_path = os.path.join(current_app.root_path, 'static', 'assets', 'data','Steps.csv')
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)

            # Read the data into a list of dictionaries
            data = list(reader)

            # Iterate over the list to rename the keys
            for row in data:
                for key in list(row.keys()):  # Use list to create a copy of keys
                    new_key = key.strip()
                    if new_key != key:
                        row[new_key] = row.pop(key)
                    if new_key == '':
                        row['Date'] = row.pop(new_key)

            # Filter the list to include only the 'Date' and 'Actual' fields
            data = [{'Date': row['Date'], 'Actual': row['Actual']} for row in data]

        return jsonify(data)

    except FileNotFoundError:
        return jsonify({"error": "CSV file not found."}), 400
    except KeyError:
        return jsonify({"error": "Required column not found in CSV file."}), 400



@activity.route('/api/heartRateData', methods=['GET'])
def get_heart_rate_data():
    """Returns heart rate data for the current user."""
    try:
        heart_rate_data = HeartRateData.query.all()
        print(heart_rate_data)
        data = [{"date": entry.date, "heart_rate": entry.heart_rate} for entry in heart_rate_data]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


############## Api Ends Here ##############


