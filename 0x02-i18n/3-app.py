#!/usr/bin/env python3
"""Flask Babel internalization and
localization module"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class
    for babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Set the default locale and timestamp based on user preferences"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def hello():
    """Render the home page with internationalized content"""
    with babel.test_request_context():
        title = babel.gettext('Welcome to Holberton')
        header = babel.gettext('Hello world!')
    return render_template("3-index.html", title=title, header=header)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
