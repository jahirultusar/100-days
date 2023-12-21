"""
Run the Flask app.

This script initializes and runs the Flask app. It creates the necessary database tables
if they do not exist and runs the app in debug mode.

Note: Make sure to run this script when you want to start the application.

Usage:
    python run.py

"""
# from flask_migrate import Migrate
from app import app, db


# db.init_app(app)
# migrate = Migrate(app, db)

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
