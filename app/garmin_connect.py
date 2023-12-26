from garminconnect import (
    Garmin,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
    GarminConnectAuthenticationError,
)

email = "tusar86@gmail.com"
password = "Tu271286!"

try:
    # Create Garmin client
    garmin_client = Garmin(email, password)
    print("Logging in...")
    garmin_client.login()
    print("Login successful")
    # Fetch activities
    activities = garmin_client.get_activities(0, 1)  # Fetch the latest activity

    # Print details of the first activity
    if activities:
        activity = activities[0]
        print(f"Activity Name: {activity['activityName']}")
        print(f"Activity Type: {activity['activityType']['typeKey']}")
        print(f"Start Time: {activity['startTimeLocal']}")
        print(f"Duration (s): {activity['duration']}")
        print(f"Distance (m): {activity['distance']}")
    else:
        print("No activities found.")

except (
    GarminConnectConnectionError,
    GarminConnectAuthenticationError,
    GarminConnectTooManyRequestsError,
) as err:
    print(f"Error occurred: {err}")
    quit()
