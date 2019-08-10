import os
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify, render_template, redirect
from flask_pymongo import PyMongo
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import scraper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
mongo = PyMongo(app, uri = "mongodb://localhost:27017/mars_app")

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
      destination_data = mongo.db.Mars.find_one()
      destination_datas = mongo.db.Marss.find_one()
      destination_datass = mongo.db.Marsss.find_one()

      return render_template("index.html", Marss = destination_data,Marsss = destination_datas, Marssss = destination_datass)
      
@app.route("/scrape")
def scrape():
  
      # Run the scrape function and save the results to a variable
  
      results = scraper.scrape_info()
      resultss = scraper.scrape_infos()
      resultsss = scraper.scrape_hem()

      # Update the Mongo database using update and upsert=True
  
      mongo.db.Mars.update({},results, upsert = True)
      mongo.db.Marss.update({},resultss,upsert = True)
      mongo.db.Marsss.update({},resultsss,upsert=True)
      
      # Redirect back to home page
      return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
