#!/usr/bin/python3
'''return hello hbnb'''
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_HBNB():
    '''returns content at flask's root'''
    return ("Hello HBNB!")


@app.route('/hbnb/')
def HBNB():
    '''returns content at /hbnb/'''
    return ("HBNB")


@app.route('/c/<text>')
def ctext(text):
    '''returns content at /c/ with arg'''
    text = text.replace("_", " ")
    return ("C " + text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
