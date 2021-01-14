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
    
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/names<br/>"
        f"/api/v1.0/passengers"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    session = Session(engine)
    
    results = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date>= "2016-08-23").\
    filter(Measurement.date <="2017-08-23").all()
    
    session.close()
    
    return ""

@app.route("/api/v1.0/stations")
def stations():
    
    session = Session(engine)
    
    return ""

@app.route("/api/v1.0/tobs")
def tobs():
    
    session = Session(engine)
    
    return ""


if __name__ == "__main__":
    app.run(debug=True)