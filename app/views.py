"""
Here are flask routes.
"""
import app.tools.mongo_tools as at
import json

from app import app
from flask import render_template, Response


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')


@app.route('/get_most_populated', methods=['POST', ])
def get_most_populated():
    # Create MongoDB connection
    cat = at.Catalog()
    # Get top-20 populated cities and transformate it into JSON format, suitable for nv.d3 graph.
    result = {'key': 'Cities by population', "color": "#4f99b4"}
    result['values'] = [{'label': '{} ({})'.format(
                                                   ' '.join([word.capitalize() for word in row['city'].split(' ')])
                                                   if ' ' in row['city'] else row['city'].capitalize(),
                                                   row['state']), 'value': row['pop']}
                        for row in json.loads(cat.get_most_populated())]
    result = json.dumps(result, indent=3)
    resp = Response(result, status=200, mimetype='application/json')
    resp.headers['Link'] = 'localhost:5000'
    return resp


@app.route('/about')
def about():
    # Page with some info about application.
    return render_template("about.html", title="About")


@app.route('/translation')
def translation():
    # Page with a text translation
    return render_template("translation.html", title='Translation')

