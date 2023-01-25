from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    gender = StringField("gender", validators=[DataRequired()])
    submit = SubmitField("submit")