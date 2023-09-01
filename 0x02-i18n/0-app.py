#!/usr/bin/env python3
"""Flask Babel internalization and localization module"""
from flask import Flask, render_template, make_response

app = Flask(__name__)


@app.route('/')
def hello():
    """This is a basic setup of flask"""
    return render_template("0-index.html")


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
