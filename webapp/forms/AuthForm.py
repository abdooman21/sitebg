from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length, EqualTo
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, ValidationError
from flask_wtf.file import FileField, FileAllowed
from webapp.models.AuthModel import User

class LoginForm(FlaskForm):
    email = StringField("email", validators=[Email()])
    username = StringField("username", validators=[Length(min=2,max=20)])
    password = PasswordField("password",validators=[DataRequired()])
    submit = SubmitField("signin") # Corrected typo: "sginin" -> "signin"

    # --- FIX IS HERE: Add **kwargs ---
    def validate(self, *, extra_validators=None, **kwargs):
        # Call the base form's validate method first, passing along extra_validators and other kwargs
        if not super().validate(extra_validators=extra_validators, **kwargs):
            return False

        # Custom validation logic: require either username or email
        if not self.username.data and not self.email.data:
            msg = "Either username or email is required."
            self.username.errors.append(msg)
            self.email.errors.append(msg)
            return False

        return True


class RegisterForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField("email", validators=[DataRequired(), Email()])
    password = PasswordField("password",validators=[DataRequired(),Length(min=5)])
    confirmpass = PasswordField("confirm password", validators=[DataRequired(),EqualTo('password',message="confirm pass and pass don't equal")])
    submit = SubmitField("signup")

    def validate_email(self,field):
       val=  User.get_by_email(field.data)
       if  val:
           raise ValidationError('Email already exists. Please choose a different one.') # Corrected message

    def validate_username(self,field):
        val = User.get_by_username(field.data)
        if  val:
            raise ValidationError('Username already exists. Please choose a different one.') # Corrected message