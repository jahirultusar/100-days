from flask import Blueprint, render_template, jsonify
from app.activity.models import StepsData
# User, Workout, Strength, Run, Fasting, Rest, CalorieIntake, CalorieBurn, CalorieDeficit, Weight

dashboard = Blueprint('dashboard', __name__)

############## Routes Starts Here ##############

# Dashborad page
# @dashboard.route('/dashboard')
# def index():
#     # Fetch data from the database, for example:
#     user_data = User.query.filter_by(username='your_username').first()
#     workout_data = Workout.query.filter_by(user_id=user_data.id).all()
#     strength_data = Strength.query.filter_by(user_id=user_data.id).all()
#     run_data = Run.query.filter_by(user_id=user_data.id).all()
#     fasting_data = Fasting.query.filter_by(user_id=user_data.id).all()
#     rest_data = Rest.query.filter_by(user_id=user_data.id).all()
#     calorie_intake_data = CalorieIntake.query.filter_by(user_id=user_data.id).all()
#     calorie_burn_data = CalorieBurn.query.filter_by(user_id=user_data.id).all()
#     calorie_deficit_data = CalorieDeficit.query.filter_by(user_id=user_data.id).all()
#     weight_data = Weight.query.filter_by(user_id=user_data.id).all()

#     return render_template('dashboard/dashboard.html', user=user_data, workouts=workout_data, strengths=strength_data, runs=run_data, fasts=fasting_data, rests=rest_data,
#                            calorie_intake=calorie_intake_data, calorie_burn=calorie_burn_data, calorie_deficit=calorie_deficit_data, weights=weight_data)

@dashboard.route('/dashboard')
def index():
    """Dashboard index route"""
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

# ############## Routes Ends Here ##############

# ############## Api Starts Here ##############
# @dashboard.route('/api/stepsData', methods=['GET'])
# def get_steps_data():
#     try:
#         steps_data = StepsData.query.all()
#         print(steps_data)
#         data = [{'date': entry.date.strftime('%Y-%m-%d'), 'steps': entry.steps} for entry in steps_data]
#         return jsonify(data)
#     except Exception as e:
#         print(f"Error fetching steps data: {e}")
#         return jsonify({'error': 'Internal Server Error'}), 500
# ############## Functions Ends Here ##############