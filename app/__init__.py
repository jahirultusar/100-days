"""
Flask Application Configuration and Initialization.

This script configures and initializes a Flask application with various extensions,
including Flask SQLAlchemy for database management, Flask Migrate for database migrations,
Flask Bcrypt for password hashing, and registers blueprints for different parts of the application.

Usage:
    This script is intended to be imported and used by other scripts or modules within the Flask app.

Example:
    from app import app, db, migrate, bcrypt

    if __name__ == '__main__':
        '''for development only'''
        app.run(debug=True)

    if __name__ == '__main__':
        '''for deployment'''
        app.run()

"""
import os
from dotenv import load_dotenv
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# App configuration
app = Flask(__name__)
load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///activity.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

# Import and register blueprints
# from app.authentication.routes import auth
from app.main.routes import main
from app.dashboard.routes import dashboard
from app.activity.routes import activity

# app.register_blueprint(auth)
app.register_blueprint(main)
app.register_blueprint(dashboard)
app.register_blueprint(activity)

# Global Error Handling
# @app.errorhandler(404)
# def page_not_found(e):
#     """Handles Global 404 errors."""
#     print(f"An unexpected error occurred: {e}")
#     return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_server_error(e):
#     """Handles Global 500 errors."""
#     print(f"An unexpected error occurred: {e}")
#     return render_template('500.html'), 500