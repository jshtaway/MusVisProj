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

class ArtistSearch(Form):
    artistName = StringField('Artist Name')

@app.route('/artist', methods=['GET','POST'])
def artist():
    form = ArtistSearch(request.form)
    artist_name = ''
    if request.method == 'POST':
        artist_name = form.artistName.data
        print(artist_name)
    return render_template('artist.html', artist_name=artist_name)


if __name__ == '__main__':
    app.run(debug=True)
