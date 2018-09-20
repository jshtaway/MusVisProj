import pandas as pd
import datetime as dt
from wtforms import Form, StringField
from flask_wtf import FlaskForm

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

# class ArtistSearch(FlaskForm):

@app.route('/artist', methods=['GET','POST'])
def artist():
    #form = ArtistSearch(request.form)
    artist_name = ''
    if request.method == 'POST':
        artist_name = request.form.data
        print(artist_name)
    # artist_events = Base.classes.artist_events
    # results = session.query(artist_events.artist_name, artist_events.city, artist_events.consert_name, artist_events.date, artist_events.lat, artist_events.lng, artist_events.popularity).filter(artist_events.artist_name == artist).all()
    # geojson = to_geojson(results)
    results = artist_name#jsonify(geojson)
    return render_template('artist.html',results=results)

@app.route('/api/<artist>')
def api(artist):
    artist_events = Base.classes.artist_events
    results = session.query(artist_events.artist_name, artist_events.city, artist_events.consert_name, artist_events.date, artist_events.lat, artist_events.lng, artist_events.popularity).filter(artist_events.artist_name == artist).all()
    return jsonify(results)

@app.route('/api_geojson/<artist>')
def api_geojson(artist):
    artist_events = Base.classes.artist_events
    results = session.query(artist_events.artist_name, artist_events.city, artist_events.consert_name, artist_events.date, artist_events.lat, artist_events.lng, artist_events.popularity).filter(artist_events.artist_name == artist).all()
    geojson = to_geojson(results)
    print("Loading GeoJSON...")
    return jsonify(geojson)

# Use the following functions to convert api info to GeoJSON
def to_geojson(results):
    geojson = {'type':'FeatureCollection', 'features':[]}
    for result in results:
        feature = {'type':'Feature',
                   'properties':{},
                   'geometry':{'type':'Point',
                               'coordinates':[]}}
        feature['geometry']['coordinates'] = [result.lng,result.lat]
        feature['properties']['name'] = result.consert_name
        feature['properties']['date'] = result.date
        feature['properties']['city'] = result.city
        feature['properties']['popularity'] = result.popularity
        geojson['features'].append(feature)
    return geojson

if __name__ == '__main__':
    app.run(debug=True)
