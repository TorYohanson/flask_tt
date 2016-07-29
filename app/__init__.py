"""
Application for test task.
Takes information about population from http://media.mongodb.org/zips.json,
stores it in MongoDB and gives a information about top-20 most populated cities on request to home directory.
"""
import app.tools.mongo_tools as at

from app import views
from flask_wtf.csrf import CsrfProtect

from flask import Flask

# Creates DB connection and loads information from http://media.mongodb.org/zips.json into MongoDB collection.
cat = at.Catalog()
cat.load_collection()

app = Flask(__name__)

# Enables CSRF protection for POST requests.
app.config.update(
    CSRF_ENABLED=True,
    DEBUG=True,
    SECRET_KEY='Tiglatpolosar'
)
CsrfProtect(app)
