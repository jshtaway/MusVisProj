import pandas as pd
import datetime as dt
from wtforms import Form, StringField

from flask import (
    Flask,
    request,
    render_template,
    jsonify)

  
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
engine = create_engine("sqlite:///db/events.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/web_structure')
def web_structure():
    return render_template('web_structure.html')

@app.route('/artist', methods=['GET','POST'])
def artist():
    #form = ArtistSearch(request.form)
    artist_name = ''
    if request.method == 'POST':
        artist_name = form.artistName.data
        print(artist_name)
    return render_template('artist.html', artist_name=artist_name)

@app.route('/api/<artist>')
def api(artist):
    artist_events = Base.classes.artist_events
    results = session.query(artist_events.artist_name, artist_events.city, artist_events.consert_name, artist_events.date, artist_events.lat, artist_events.lng, artist_events.popularity).filter(artist_events.artist_name == artist).all()
    return render_template('artist.html',jsonify(geojson))

@app.route('/api_geojson/<artist>')
def api_geojson(artist):
    artist_events = Base.classes.artist_events
    results = session.query(artist_events.artist_name, artist_events.city, artist_events.consert_name, artist_events.date, artist_events.lat, artist_events.lng, artist_events.popularity).filter(artist_events.artist_name == artist).all()
    geojson = to_geojson(results)
    print("Loading GeoJSON...")
    return jsonify(geojson)


if __name__ == '__main__':
    app.run(debug=True)
