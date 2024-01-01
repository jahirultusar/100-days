
from flask import Blueprint, render_template
from app.activity.models import GarminData


dashboard = Blueprint('dashboard', __name__)

############## Routes Starts Here ##############


@dashboard.route('/dashboard')
def index():
    """Dashboard index route"""
    last_sync_record = GarminData.query.order_by(GarminData.last_sync.desc()).first()
    if last_sync_record is not None:
        last_sync = last_sync_record.last_sync.strftime('%d-%m-%Y %H:%M:%S')
    else:
        last_sync = None
    return render_template('dashboard/dashboard.html', last_sync=last_sync)
@dashboard.route('/dashboard/user')
def user():
    """Dashboard user route"""
    return render_template('dashboard/user.html')

@dashboard.route('/dashboard/log')
def log():
    """Dashboard activity log route"""
    return render_template('dashboard/log.html')

@dashboard.route('/dashboard/tables')
def tables():
    """Dashboard tables route"""
    return render_template('dashboard/data_tables.html')

@dashboard.route('/dashboard/icons')
def icons():
    """Dashboard icons route"""
    return render_template('dashboard/icons.html')

# ############## Routes Ends Here ##############

