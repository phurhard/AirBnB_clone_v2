#!/usr/bin/python3
"""this is an extension of 1-hbnb-route,
it prints hbnb on a new route
and also prints the value of the text
variable"""
from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """This script returns hello HBNb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """this scripts returns HBNB when the url is entered"""
    return "HBNB"


@app.route('/c/<variable>', strict_slashes=False)
def c_text(variable):
    """ This function returns the text added at the url"""
    text = escape(variable.replace('_', ' '))
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """ This fuction return python and other string"""
    user_text = escape(text.replace('_', ' '))
    return f"Python {user_text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays number is n only if n is an integer"""
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def numberTemplate(n):
    """Prints an HTML template if n is integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def EvenOddNumber(n):
    """Prints an HTML document with description of number"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    # python -m web-flask.0-hello_route
    app.run(host="0.0.0.0", port=5000)
