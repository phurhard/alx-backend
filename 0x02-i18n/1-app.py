#!/usr/bin/env python3
"""Flask Babel internalization and localization module"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# def get_locale():
#     """Set the default locale and timestamp"""
#     return request.accept_languages.best_match(app.config['LANGUAGES'])


# def get_timezone():
#     return user.timezone


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def hello():
    """This is a basic setup of flask"""
    return render_template("1-index.html")


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=1)
