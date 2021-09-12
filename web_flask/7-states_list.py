#!/usr/bin/python3
'''module for storing flask'''
from flask import Flask, render_template
from models.__init__ import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    '''returns list of states currently stored'''
    models = storage.all(State)
    template = '7-states_list.html'
    return render_template(template, models=models)


@app.teardown_appcontext
def teardown_db_connection(exception):
    '''closes ORM connection'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
