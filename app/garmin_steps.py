from datetime import datetime

# garmin_connect.py
from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
    GarminConnectAuthenticationError,
)

class GarminClient:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client = Garmin(username, password)

    def get_steps_by_day(self):
        try:
            # Authenticate with Garmin Connect
            self.client.login()

            # Get today's date
            today = datetime.today().strftime('%Y-%m-%d')

            # Fetch steps data for today
            steps_data = self.client.get_steps_data(today)

            return steps_data

        except (
            GarminConnectConnectionError,
            GarminConnectAuthenticationError,
            GarminConnectTooManyRequestsError,
        ) as err:
            print(f"Error: {err}")
            return None
