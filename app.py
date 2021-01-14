# import dependencies
from flask import Flask
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    
    return "Welcome to my 'Home' page!"

@app.route("/api/v1.0/precipitation")
def precipitation():
  
    return "Welcome to my 'About' page!"

@app.route("/api/v1.0/stations")
def stations():
  
    return "Welcome to my 'About' page!"

@app.route("/api/v1.0/tobs")
def tobs():
  
    return "Welcome to my 'About' page!"


if __name__ == "__main__":
    app.run(debug=True)