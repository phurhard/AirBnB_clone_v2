#!/usr/bin/python3
"""this is an extension of 1-hbnb-route,
it prints hbnb on a new route
and also prints the value of the text
variable"""
from flask import Flask, escape
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


if __name__ == "__main__":
    # python -m web-flask.0-hello_route
    app.run(host="0.0.0.0", port=5000)
