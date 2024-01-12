#!/usr/bin/env python3
"""Flask Babel internalization and localization module"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
BABEL_DEFAULT = "en"


@babel.localeselector
def get_locale():
    """Set the default locale and timestamp"""
    if "locale" in request.args:
        req_locale = request.args["locale"]

        if req_locale in app.config["LANGUAGES"]:
            return req_locale
    return BABEL_DEFAULT


@app.route('/')
def hello():
    """This is a basic setup of flask"""
    title = _('Welcome to Holberton')
    header = _('Hello world!')
    return render_template("4-index.html")


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
