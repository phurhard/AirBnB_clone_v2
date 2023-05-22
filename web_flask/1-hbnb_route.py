#!/usr/bin/python3
"""this is an extension of 0-hello hbnb, 
it prints hbnb on a new route"""
from flask import Flask
app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello():
    """This script returns hello HBNb"""
    return "Hello HBNB!"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """this scripts returns HBNB when the url is entered"""
    return "HBNB"
if __name__ == "__main__":
    #python -m web-flask.0-hello_route
    app.run(host="0.0.0.0", port=5000)
