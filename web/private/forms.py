from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class PrivateForm(FlaskForm):
    value = StringField('Value', validators=[DataRequired()], render_kw={"placeholder": "Value"})
