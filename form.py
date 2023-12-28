from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField(label="Cafe Location", validators=[DataRequired()])
    open_time = StringField(label='Openning time e.g 8AM', validators=[DataRequired()])
    closing_time = StringField(label="Closing time e.g 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField(label="Coffee Rating", validators=[DataRequired()], choices=[0, 1, 2, 3, 4, 5])
    wifi_rating = SelectField(label="Wifi Rating", validators=[DataRequired()], choices=[0, 1, 2, 3, 4, 5])
    power_outlet = SelectField(label="Power Outlet Rating", validators=[DataRequired()], choices=[0, 1, 2, 3, 4, 5])
    submit = SubmitField('Submit')