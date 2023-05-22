#!/usr/bin/python3
"""This script is the strt of flask, it
starts a flask app and prints hello hbnb to the interface of
the web browser"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """This script starts a flask app and prints hello HBNB"""
    return "Hello HBNB!"


if __name__ == "__main__":
    # python -m web-flask.0-hello_route
    app.run(host="0.0.0.0", port=5000)
