from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class LogbookForm(FlaskForm):
    first = StringField('first', validators=[DataRequired()])
    last = StringField('last', validators=[DataRequired()])
