#!/usr/bin/python3
'''module for storing flask'''
from flask import Flask, render_template
from models.__init__ import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states_list():
    '''returns list of states currently stored'''
    models = storage.all(State)
    template = '7-states)list.html'
    return render_template(template, models=models)


@app.route('/states/<id>')
def states_id_list(id):
    '''returns list of cities by states currently stored'''
    models = storage.all(State)
    template = '9-states.html'

    if "State.{}".format(id) in models:
        state = models.pop("State.{}".format(id))
    else:
        return ("<h1>Not found!</h1>")
    return render_template(template, state=state)


@app.teardown_appcontext
def teardown_db_connection(exception):
    '''closes ORM connection'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
