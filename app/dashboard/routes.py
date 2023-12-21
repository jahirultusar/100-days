from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__)



# Dashborad page
@dashboard.route('/dashboard')
def index():
    """Dashboard landing route"""
    return render_template('dashboard.html')
