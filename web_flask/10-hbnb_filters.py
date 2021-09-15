#!/usr/bin/python3
'''module for storing flask'''
from flask import Flask, render_template
from models.engine import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def states_list():
    '''returns list of states currently stored'''

    all_amenities = storage.all(Amenity)
    template = '10-hbnb_filters.html'
    all_stat = storage.all(State)
    return render_template(template, states=all_stat, amenities=all_amenities)


@app.teardown_appcontext
def teardown_db_connection(exception):
    '''closes ORM connection'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
