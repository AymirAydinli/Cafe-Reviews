from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
import random
import os
from form import CafeForm, UpdateCafeForm, SearchCafe
from config import db, app
from models import CafeDB
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


Bootstrap5(app)

# Connect to DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
db.init_app(app)

# Create the tables
with app.app_context():
    db.create_all()

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = CafeDB(name=form.cafe.data,
                          map_url=form.location_url.data,
                          img_url=form.image_link.data,
                          location=form.location.data,
                          has_sockets=form.sockets.data,
                          has_toilet=form.toilet.data,
                          has_wifi=form.wifi.data,
                          can_take_calls=form.calls.data,
                          seats=form.seats.data,
                          coffee_price=form.price.data
                          )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    cafe = db.get_or_404(CafeDB, id)
    form = UpdateCafeForm(
        sockets=cafe.has_sockets,
        toilet=cafe.has_toilet,
        wifi=cafe.has_wifi,
        calls=cafe.can_take_calls,
        price=cafe.coffee_price
    )
    if form.validate_on_submit():
        cafe.has_sockets = form.sockets.data
        cafe.has_toilet = form.toilet.data
        cafe.has_wifi = form.wifi.data
        cafe.can_take_calls = form.calls.data
        cafe.coffee_price = form.price.data
        db.session.commit()
        return redirect(url_for("cafes"))
    return render_template('update.html', form=form)


@app.route('/delete', methods=['GET'])
def delete():
    cafe_id = request.args.get("id")
    cafe = db.get_or_404(CafeDB, cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    redirect(url_for('home'))


@app.route('/search', methods=["GET", "POST"])
def search():
    form = SearchCafe()
    if form.validate_on_submit():
        location = form.location.data
        try:
            searched_cafes = db.session.execute(db.select(CafeDB).where(CafeDB.location == location)).scalars().all()
        except:
            return 404
        return render_template("cafes.html", cafes=searched_cafes, is_search=True)

    return render_template("search.html", form=form)


@app.route('/random_cafe')
def random_cafe():
    result = db.session.execute(db.select(CafeDB)).scalars()
    cafes = result.all()
    rand_cafe = random.choice(cafes)
    print(rand_cafe)
    return render_template('random.html', cafe=rand_cafe)


@app.route('/cafes')
def cafes():
    result = db.session.execute(db.select(CafeDB)).scalars()
    all_cafes = result.all()
    print(all_cafes)
    return render_template('cafes.html', cafes=all_cafes, is_search=False)


if __name__ == '__main__':
    app.run(debug=True)
