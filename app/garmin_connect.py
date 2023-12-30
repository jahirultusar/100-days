
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, current_app
from datetime import date, timedelta
from datetime import date
# from app.activity.models import StepsData


from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectAuthenticationError,
    GarminConnectTooManyRequestsError,
)


load_dotenv()
app = Flask(__name__)


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


# @app.route('/api/test', methods=['GET'])
# def fetch_garmin_activities():
#     """Fetches steps data from Garmin Connect API."""
#     try:
#         # Create Garmin client
#         garmin_client = garmin_login()

#         # Fetch activities
#         activities = garmin_client.get_activities(0, 1)  # Fetch the latest activity

#         # Print details of the first activity
#         if activities:
#             activity = activities[0]
#             filtered_activity = {
#                 'Activity Date': activity['startTimeLocal'],
#                 'Activity Name': activity['activityName'],
#                 'Activity Type': activity['activityType']['typeKey'],
#                 'Duration (s)': activity['duration'],
#                 'Distance (m)': activity['distance'],
#             }
#             return jsonify(filtered_activity)

#     except (
#         GarminConnectConnectionError,
#         GarminConnectAuthenticationError,
#         GarminConnectTooManyRequestsError,
#     ) as err:
#         return jsonify(f"No activities found: {err}")




# @app.route('/api/test', methods=['GET'])
# def test():
#     try:
#         garmin_client = garmin_login()

#         today = date.today()
#         steps_data = garmin_client.get_steps_data(today.isoformat())

#         # Calculate total steps
#         total_steps = sum(item['steps'] for item in steps_data)

#         return jsonify({'total_steps': total_steps})
#     except (
#         GarminConnectConnectionError,
#         GarminConnectAuthenticationError,
#         GarminConnectTooManyRequestsError,
#     ) as err:
#         return jsonify(f"No activities found: {err}")
# import csv

# @app.route('/api/test', methods=['GET'])
# def fetch_steps_from_csv():
#     """Fetches steps data from a CSV file."""
#     try:
#         # Open the CSV file
#         file_path = os.path.join(current_app.root_path, 'static', 'assets', 'data','Steps.csv')
#         with open(file_path, 'r', encoding='utf-8-sig') as file:
#             reader = csv.DictReader(file)

#             # Read the data into a list of dictionaries
#             data = list(reader)

#             # Iterate over the list to rename the keys
#             for row in data:
#                 for key in list(row.keys()):  # Use list to create a copy of keys
#                     new_key = key.strip()
#                     if new_key != key:
#                         row[new_key] = row.pop(key)
#                     if new_key == '':
#                         row['Date'] = row.pop(new_key)

#             # Filter the list to include only the 'Date' and 'Actual' fields
#             data = [{'Date': row['Date'], 'Actual': row['Actual']} for row in data]

#         return jsonify(data)

#     except FileNotFoundError:
#         return jsonify({"error": "CSV file not found."}), 400
#     except KeyError:
#         return jsonify({"error": "Required column not found in CSV file."}), 400

@app.route('/api/test', methods=['GET'])
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
            activity = activities[0]
            filtered_activity = {
                'Activity Date': activity['startTimeLocal'],
                'Activity Name': activity['activityName'],
                'Activity Type': activity['activityType']['typeKey'],
                'Duration (h)': round(activity['duration'] / 3600, 2),  # Convert to hours and round off to 2 decimal places
                'Distance (km)': round(activity['distance'] / 1000, 2),
            }

        # Fetch health stats
        health_stats = garmin_client.get_stats(today.isoformat())
        if health_stats:
            filtered_health_stats = {
                'Source': health_stats['source'],
                'Date': health_stats['calendarDate'],
                'Last Sync': health_stats['lastSyncTimestampGMT'],
                'Daily Step Goal': health_stats['dailyStepGoal'],
                'Total Steps': health_stats['totalSteps'],
                'Net Calories Goal': health_stats['netCalorieGoal'],
                'Active Calories': health_stats['activeKilocalories'],
                'Burned Calories': health_stats['burnedKilocalories'],
                'Consumed Calories': health_stats['consumedKilocalories'],
                'Calorie Deficit': health_stats['netRemainingKilocalories'] - health_stats['consumedKilocalories'],
                'Intensity Minutes Goal': health_stats['intensityMinutesGoal'],
                'Active Minutes': round(health_stats['activeSeconds'] / 60), # Convert to minutes
                'Average Stress Level': health_stats['averageStressLevel'],
                'Body Battery': health_stats['bodyBatteryMostRecentValue'],
                'Floor Climbed:': round(health_stats['floorsAscended']),
                'Max Heart Rate': health_stats['maxHeartRate'],
                'Resting Heart Rate': health_stats['restingHeartRate'],
                'Sleeping Time': round(health_stats['sleepingSeconds'] / 3600, 2),
            }

        # Combine all data into one dictionary
        data = {
            'activity_data': filtered_activity,
            'health_stats': filtered_health_stats,
        }

        return jsonify(data)

    except (
        GarminConnectConnectionError,
        GarminConnectAuthenticationError,
        GarminConnectTooManyRequestsError,
    ) as err:
        return jsonify(f"No data found: {err}")

@app.route('/api/stats', methods=['GET'])
def stats():
    """Fetches stats from Garmin Connect API."""
    try:
        # Create Garmin client
        garmin_client = garmin_login()

        # Fetch steps data
        today = date.today()

        # Fetch health stats
        health_stats = garmin_client.get_stats(today.isoformat())

        return jsonify(health_stats)

    except (
        GarminConnectConnectionError,
        GarminConnectAuthenticationError,
        GarminConnectTooManyRequestsError,
    ) as err:
        return jsonify(f"No data found: {err}")





if __name__ == '__main__':
    app.run(debug=True)



