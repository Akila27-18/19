from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange

class DonationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    amount = IntegerField('Amount (₹)', validators=[DataRequired(), NumberRange(min=10, message="Minimum donation is ₹10")])
    cause = SelectField('Cause', choices=[
        ('Education', 'Education'),
        ('Healthcare', 'Healthcare'),
        ('Environment', 'Environment'),
        ('Animal Welfare', 'Animal Welfare')
    ], validators=[DataRequired()])
    submit = SubmitField('Donate')
