#!/usr/bin/env python3
"""Flask Babel internalization and localization module"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Set the default locale and timestamp"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def hello():
    """This is a basic setup of flask"""
    return render_template("2-index.html")


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
