""" python file containing flask form for admin account creation """

import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, DateField
from wtforms.validators import Email, ValidationError, DataRequired, Length, EqualTo


def validate_name(form, name):
    """ Validator to check forbidden characters in names """

    excluded_chars = "*?!'^+%&/()=}][{$#@<>"

    for char in name.data:
        if char in excluded_chars:
            raise ValidationError(f"Character {char} is not allowed")


def validate_password(form, password):
    """ Validator to check password format """

    pattern = re.compile(r'(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-z0-9])')

    if not pattern.match(password.data):
        raise ValidationError("Password must contain at least 1 digit, "
                              "1 lowercase, 1 uppercase word character and "
                              "1 special character.")


#
class AdminSignUpForm(FlaskForm):
    """ Signup Form containing all the details needed for a user to create an account"""

    email = StringField(validators=[DataRequired(), Email()])
    first_name = StringField(validators=[DataRequired(), validate_name])
    last_name = StringField(validators=[DataRequired(), validate_name])
    password = PasswordField(validators=[DataRequired(), Length(min=8), validate_password])
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo('password', message='Both password fields '
                                                                                             'must be equal')])
    birthday = DateField(validators=[DataRequired()])
    address = StringField(validators=[DataRequired()])
    submit = SubmitField()
