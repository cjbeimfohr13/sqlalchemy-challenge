# import dependencies
from flask import Flask,jsonify
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

Station= Base.classes.station
Measurement= Base.classes.measurement

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
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    session = Session(engine)
    
    results = session.query(Measurement.date,Measurement.prcp).filter(Measurement.date>= "2016-08-23").\
    filter(Measurement.date <="2017-08-23").all()
    
    session.close()
    
    precipitation = []
    for date,prcp in results:
        precipitation_dict = {}
        precipitation_dict["date"] = results[0]
        precipitation_dict["prcp"] = results[1]
        precipitation.append(precipitation_dict)

    return jsonify(precipitation)
    

@app.route("/api/v1.0/stations")
def stations():
    
    session = Session(engine)
    
    results = session.query(Measurement.station).group_by(Measurement.station).all()
    
    session.close()
    
    stations = [] 
    for station in results: 
        stations_dict={}
        stations["station"]=results[0]
        stations.append(stations_dict)
        
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    
    session = Session(engine)
    
    results=session.query(Measurement.date,Measurement.tobs).filter(Measurement.date>= "2016-08-23").\
        filter(Measurement.date <="2017-08-23").\
        filter(Measurement.station=='USC00519281').all()
    
    tobs = [] 
    for r in results: 
        tobs_dict={}
        tobs_dict["date"]=results[0]
        tobs_dict["tobs"]=results[1]
        tobs.append(tobs_dict) 
    
    return jsonify(tobs)

@app.route("/api/v1.0/<start>")
def start():
    
    session = Session(engine)
    results_min_max_avg=session.query(func.avg(Measurement.tobs),func.min(Measurement.tobs),func.max(Measurement.tobs)).\
    filter(Measurement.date>="2016-08-23").all()
    
    start_tobs=[]
    for result in results_min_max_avg:
        dict_start_tobs={}
        dict_start_tobs["Min"]=results_min_max_avg[1]
        dict_start_tobs["Max"]=results_min_max_avg[2]
        dict_start_tobs["Avg"]=results_min_max_avg[0]
        start_tobs.append(dict_start_tobs)
    
    return jsonify(start_tobs)

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    
    session = Session(engine)
    start_end_min_max_avg=session.query(func.avg(Measurement.tobs),func.min(Measurement.tobs),func.max(Measurement.tobs)).\
    filter(Measurement.date>="2016-08-23").\
    filter(Measurement.date<="2017-08-23").all()
    
    start_end_tobs=[]
    for result in start_end_min_max_avg:
        dict_start_end_tobs={}
        dict_start_end_tobs["Min"]=start_end_min_max_avg[1]
        dict_start_end_tobs["Max"]=start_end_min_max_avg[2]
        dict_start_end_tobs["Avg"]=start_end_min_max_avg[0]
        start_end_tobs.append(dict_start_end_tobs)
        
    return jsonify(start_end_tobs)


if __name__ == "__main__":
    app.run(debug=True)