from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired
import csv
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField(label="Cafe Location", validators=[DataRequired()])
    open_time = StringField(label='Openning time e.g 8AM', validators=[DataRequired()])
    closing_time = StringField(label="Closing time e.g 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField(label="Coffee Rating", validators=[DataRequired()], choices=[0, 1, 2, 3, 4, 5])
    wifi_rating = SelectField(label="Wifi Rating", validators=[DataRequired()], choices=[0, 1, 2, 3, 4, 5])
    power_outlet = SelectField(label="Power Outlet Rating", validators=[DataRequired()], choices=[0, 1, 2, 3, 4, 5])
    submit = SubmitField('Submit')



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        row = [form.cafe.data, form.location.data, form.open_time.data, form.closing_time.data, form.coffee_rating.data, form.wifi_rating.data, form.power_outlet.data]
        with open('cafe-data.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(row)
        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)