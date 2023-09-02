#!/usr/bin/env python3
"""Flask Babel internalization and localization module"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
            print(f'here   is the laaang {req_locale}')
            return req_locale
    return BABEL_DEFAULT


@app.before_request
def before_request():
    """Run before all other functions"""
    user = get_user()
    # print(f'get user: {get_user()}')
    g.user = user


def get_user():
    """Users login simulation"""
    if 'login_as' not in request.args.keys():
        return None
    else:
        id = request.args["login_as"]
        id = int(id)
        return users.get(id, None)


@app.route('/')
def hello():
    """This is a basic setup of flask"""
    return render_template("5-index.html", username=g.user["name"])


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=1)
