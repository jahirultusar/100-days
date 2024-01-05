from datetime import date
from flask import jsonify
from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectAuthenticationError,
    GarminConnectTooManyRequestsError,
)
def fetch_garmin_data():
    email = "tusar86@gmail.com"
    password = "Tu271286!"

    # Authenticate with GarminConnect
    garmin_client = Garmin(email, password)
    garmin_client.login()
    print("Logged in")

    # Fetch steps data for today
    today = date.today()
    steps_data = garmin_client.get_steps_data(today.isoformat())
    print(steps_data)

    return jsonify(steps_data)
fetch_garmin_data()