from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, RadioField, validators
import requests
import json
import os
import codecs
import pandas as pd
from datetime import datetime
from elasticsearch import Elasticsearch
from pymongo import MongoClient # Database connector
from bson.objectid import ObjectId # For ObjectId to work

#APP settings
app = Flask(__name__)


#CONNECT TO MONGODB
client = MongoClient('localhost', 27017)    #Configure the connection to the database
db = client.mdh                             #Select the database
feddata = db.feddata                        #Select the collection

title = "MDH metadata manager"
heading = "List Details"
#modify=ObjectId()

@app.route("/home")
def home():
	return render_template('index.html',t=title,h=heading)

@app.route("/list")
def lists ():
    #Display the all Studies
    feddata_l = feddata.find()
    a1="active"
    return render_template('index.html',a1=a1,feddata=feddata_l,t=title,h=heading)

@app.route("/search", methods=['GET'])
def search():
	#Searching a Task with various references
	key=request.values.get("key")
	refer=request.values.get("refer")
	if(key=="_id"):
		feddata_l = feddata.find({refer:ObjectId(key)})
	else:
		feddata_l = feddata.find({refer:key})
	return render_template('searchlist.html',feddata=feddata_l,t=title,h=heading)


@app.route("/about")
def about():
	return render_template('credits.html',t=title,h=heading)




if __name__ == "__main__":
    app.secret_key='secret123'
    app.run('0.0.0.0',5003,debug=True)
