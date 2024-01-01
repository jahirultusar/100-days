
from flask import Blueprint, render_template
from sqlalchemy import desc
from app import db
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

    # Find and list last Activity
    # last_activity = GarminData.query.all()
    last_activity = (db.session.query(GarminData)
                .group_by(GarminData.activity_date)
                .order_by(desc(GarminData.activity_date))
                .all())

    return render_template('dashboard/dashboard.html', last_sync=last_sync, last_activity=last_activity)

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

