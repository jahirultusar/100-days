from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__)



# Dashborad page
@dashboard.route('/dashboard')
def index():
    """Dashboard landing route"""
    return render_template('dashboard/dashboard.html')

@dashboard.route('/dashboard/user')
def user():
    """Dashboard user route"""
    return render_template('dashboard/user.html')

@dashboard.route('/dashboard/tables')
def tables():
    """Dashboard tables route"""
    return render_template('dashboard/data_tables.html')

@dashboard.route('/dashboard/icons')
def icons():
    """Dashboard icons route"""
    return render_template('dashboard/icons.html')