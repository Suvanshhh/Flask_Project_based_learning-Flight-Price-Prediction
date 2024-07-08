from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField
) # importing field to get input
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Optional,
    EqualTo
) # importing validators

# wtforms is compliant with pythonic coding style
# Here, we work with forms as in python using objects and attributes.
# Treat forms as python classes

# SignUp form class:
class SignupForm(FlaskForm):
    # treating as objects and attributes.
    username = StringField(
        # providing labels and validators.
        "Username", validators=[DataRequired(), Length(2, 30)]
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )
    gender = SelectField(
        "Gender",
        choices=["Male", "Female", "Other"],
        validators=[Optional()]
    )
    dob = DateField(
        "Date of Birth",
        validators=[Optional()]
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(5, 25)]
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), Length(5, 25), EqualTo("password")]
    )
    submit = SubmitField(
        "SignUp"
    )


#Login form Class
class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(5, 25)]
    )

    remember_me = BooleanField("Remember Me")

    submit = SubmitField(
        "LogIn"
    )
