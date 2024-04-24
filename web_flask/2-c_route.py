#!/usr/bin/python3
""" Write a script that starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """Displays 'C' followed by the text with underscores replaced by spaces"""
    return f"C {text.replace('_', ' ')}"  # Using f-string (optional)


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text="is cool"):
    """Displays 'Python' followed by the text with underscores replaced by spaces (defaults to 'is cool')"""
    return f"Python {text.replace('_', ' ')}"  # Using f-string (optional)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
