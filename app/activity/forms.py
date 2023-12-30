

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, SelectMultipleField, BooleanField, TextAreaField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length, Optional


####################### Activity Forms #######################

class AddActivityForm(FlaskForm):
    """Form to add an activity"""
    activity_name = StringField('Activity Name', validators=[DataRequired()])
    activity_date = StringField('Activity Date', validators=[DataRequired()])
    activity_desc = TextAreaField('Activity Description', validators=[Optional()])
    activity_type = SelectField('Activity Type', choices=[('1', 'Strength'), ('2', 'Run'), ('3', 'HIIT'), ('4', 'Other')])
    activity_duration = IntegerField('Activity Duration', validators=[DataRequired()])
    submit = SubmitField('Add Activity')

class EditActivityForm(FlaskForm):
    """Form to edit an activity"""
    activity_name = StringField('Activity Name', validators=[DataRequired()])
    activity_date = StringField('Activity Date', validators=[DataRequired()])
    activity_desc = TextAreaField('Activity Description', validators=[Optional()])
    activity_type = SelectField('Activity Type', choices=[('1', 'Strength'), ('2', 'Run'), ('3', 'HIIT'), ('4', 'Other')])
    activity_duration = IntegerField('Activity Duration', validators=[DataRequired()])
    submit = SubmitField('Edit Activity')

class DeleteActivityForm(FlaskForm):
    """Form to delete an activity"""
    submit = SubmitField('Delete Activity')

####################### Activity Forms Ends#######################

####################### stepsData Forms #######################
class AddStepsForm(FlaskForm):
    """Form to add steps"""
    steps = IntegerField('Steps', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Add Steps')

class EditStepsForm(FlaskForm):
    """Form to edit steps"""
    steps = IntegerField('Steps', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Edit Steps')
####################### stepsData Forms Ends #######################

####################### Strength Forms #######################

class AddStrengthForm(FlaskForm):
    """Form to add a strength workout"""
    strength_name = SelectMultipleField('Workout Name', choices=[('1', 'Chest'), ('2', 'Back'), ('3', 'Leg'), ('4', 'Core'), ('5', 'Bicep'), ('6', 'Tricep'), ('7', 'Shoulder'), ('8', 'Other')], validators=[DataRequired()])
    strength_date = StringField('Workout Date', validators=[DataRequired()])
    strength_desc = TextAreaField('Workout Description', validators=[Optional()])
    strength_duration = IntegerField('Workout Duration', validators=[DataRequired()])
    submit = SubmitField('Add Workout')

class EditStrengthForm(FlaskForm):
    """Form to edit a strength workout"""
    strength_name = SelectMultipleField('Workout Name', choices=[('1', 'Chest'), ('2', 'Back'), ('3', 'Leg'), ('4', 'Core'), ('5', 'Bicep'), ('6', 'Tricep'), ('7', 'Shoulder'), ('8', 'Other')], validators=[DataRequired()])
    strength_date = StringField('Workout Date', validators=[DataRequired()])
    strength_desc = TextAreaField('Workout Description', validators=[Optional()])
    strength_duration = IntegerField('Workout Duration', validators=[DataRequired()])
    submit = SubmitField('Edit Workout')

class DeleteStrengthForm(FlaskForm):
    """Form to delete a strength workout"""
    submit = SubmitField('Delete Workout')

####################### Strength Forms Ends #######################

####################### Run Forms #######################

class AddRunForm(FlaskForm):
    """Form to add a run"""
    run_type = SelectField('Run Type', choices=[('1', 'Long'), ('2', 'Tempo'), ('3', 'Interval'), ('4', 'Other')], validators=[DataRequired()])
    run_date = StringField('Run Date', validators=[DataRequired()])
    run_desc = TextAreaField('Run Description', validators=[Optional()])
    run_duration = IntegerField('Run Duration', validators=[DataRequired()])
    run_distance = IntegerField('Run Distance', validators=[DataRequired()])
    submit = SubmitField('Add Run')

class EditRunForm(FlaskForm):
    """Form to edit a run"""
    run_type = SelectField('Run Type', choices=[('1', 'Long'), ('2', 'Tempo'), ('3', 'Interval'), ('4', 'Other')], validators=[DataRequired()])
    run_date = StringField('Run Date', validators=[DataRequired()])
    run_desc = TextAreaField('Run Description', validators=[Optional()])
    run_duration = IntegerField('Run Duration', validators=[DataRequired()])
    run_distance = IntegerField('Run Distance', validators=[DataRequired()])
    submit = SubmitField('Edit Run')

class DeleteRunForm(FlaskForm):
    """Form to delete a run"""
    submit = SubmitField('Delete Run')

####################### Run Forms Ends #######################

####################### Fasting Forms #######################
class AddFastingForm(FlaskForm):
    """Form to add a fasting day"""
    fasting_date = StringField('Fasting Date', validators=[DataRequired()])
    fasting_desc = TextAreaField('Fasting Description', validators=[Optional()])
    fasting_duration = IntegerField('Fasting Duration', validators=[DataRequired()])
    submit = SubmitField('Add Fasting')

class EditFastingForm(FlaskForm):
    """Form to edit a fasting day"""
    fasting_date = StringField('Fasting Date', validators=[DataRequired()])
    fasting_desc = TextAreaField('Fasting Description', validators=[Optional()])
    fasting_duration = IntegerField('Fasting Duration', validators=[DataRequired()])
    submit = SubmitField('Edit Fasting')

class DeleteFastingForm(FlaskForm):
    """Form to delete a fasting day"""
    submit = SubmitField('Delete Fasting')

####################### Fasting Forms Ends #######################

####################### Calorie Intake Forms #######################
class AddCalorieIntakeForm(FlaskForm):
    """Form to add a calorie intake"""
    calories_in = IntegerField('Calories In', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Add Calorie Intake')

class EditCalorieIntakeForm(FlaskForm):
    """Form to edit a calorie intake"""
    calories_in = IntegerField('Calories In', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Edit Calorie Intake')

class DeleteCalorieIntakeForm(FlaskForm):
    """Form to delete a calorie intake"""
    submit = SubmitField('Delete Calorie Intake')

####################### Calorie Intake Forms Ends #######################
####################### Calorie Burn Forms #######################
class AddCalorieBurnForm(FlaskForm):
    """Form to add a calorie burn"""
    calories_out = IntegerField('Calories Out', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Add Calorie Burn')

class EditCalorieBurnForm(FlaskForm):
    """Form to edit a calorie burn"""
    calories_out = IntegerField('Calories Out', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Edit Calorie Burn')

class DeleteCalorieBurnForm(FlaskForm):
    """Form to delete a calorie burn"""
    submit = SubmitField('Delete Calorie Burn')

####################### Calorie Burn Forms Ends #######################

####################### Weight Forms #######################
class AddWeightForm(FlaskForm):
    """Form to add a weight"""
    weight = FloatField('Weight', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Add Weight')