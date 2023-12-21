"""
Main Module for Application Landing Page.

This module defines the main functionality of the application's landing page, including
routes for rendering the index page.

Routes:
    - main: Blueprint for managing routes related to the main application.

Usage:
    This module is part of the Flask application and handles the landing page.
"""

from flask import Blueprint, render_template


main = Blueprint('main', __name__)

# Landing page
@main.route('/')
def index():
    """Landing Page Route in the Main Module."""
    return render_template('index.html')


