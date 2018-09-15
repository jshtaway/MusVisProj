import pandas as pd
import datetime as dt

from flask import (
    Flask,
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

@app.route('/About')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
