#!/usr/bin/python3
'''return hello hbnb'''
from flask import Flask, render_template


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


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def pytext(text):
    '''returns content at /python with arg & default'''
    text = text.replace("_", " ")
    return ("Python " + text)


@app.route('/number/<int:num>')
def numroute(num):
    '''returns content at /number/int:number'''
    return ("{} is a number".format(num))


@app.route('/number_template/<int:num>')
def numtemplate(num):
    '''returns content at /number_template/<number> w html render'''
    return render_template('5-number.html', num=num)


@app.route('/number_odd_or_even/<int:num>')
def number_odd_even(num):
    '''return content at /number_odd_or_even/<num> w html render'''
    return render_template('6-number_odd_or_even.html', num=num)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
