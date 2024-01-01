from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField, BooleanField, FloatField
from wtforms.validators import DataRequired

#choices = ['✅', '❌']


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = URLField(label="Cafe Location URL")
    image_link = URLField(label="Cafe Images")
    location = StringField(label="Cafe Location")
    sockets = SelectField(label="Socket")
    toilet = SelectField(label="Toilet")
    wifi = SelectField(label="Wifi")
    calls = SelectField(label="Calls")
    seats = SelectField(label="Seat Count", validators=[DataRequired()],
                        choices=["0-10", "10-20", "20-30", "30-50", "50+"])
    price = StringField(label="Price", validators=[DataRequired()])
    submit = SubmitField('Submit')


class UpdateCafeForm(FlaskForm):
    sockets = SelectField(label="Socket")
    toilet = SelectField(label="Toilet")
    wifi = SelectField(label="Wifi")
    calls = SelectField(label="Calls")
    seats = SelectField(label="Seat Count", validators=[DataRequired()],
                        choices=["0-10", "10-20", "20-30", "30-50", "50+"])
    price = StringField(label="Price", validators=[DataRequired()])
    submit = SubmitField('Submit')


class SearchCafe(FlaskForm):
    location = StringField(label="Cafe Location", validators=[DataRequired()])
    submit = SubmitField("Search")
