"""
Run the Flask app.

This script initializes and runs the Flask app. It creates the necessary database tables
if they do not exist and runs the app in debug mode.

Note: Make sure to run this script when you want to start the application.

Usage:
    python run.py

"""
from flask_migrate import Migrate
from apscheduler.schedulers.background import BackgroundScheduler
from app import app, db
from app.activity.routes import job


# db.init_app(app)
migrate = Migrate(app, db)


# Create a scheduler
scheduler = BackgroundScheduler()

# Schedule the job in AM
scheduler.add_job(job, 'cron', hour=11, minute=55)

# Schedule the job in PM
scheduler.add_job(job, 'cron', hour=23, minute=55)

# Start the scheduler
scheduler.start()


if __name__ == '__main__':
    with app.app_context():
        # Run the job once
        db.create_all()
    app.run(host='0.0.0.0', port=5001)