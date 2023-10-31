#!/usr/bin/env python3
"""Module with Babel, locale selection,parametrized template,URL parameter."""

from flask import Flask, render_template, request
from flask_babel import Babel
from os import getenv


app = Flask(__name__, static_url_path='')
babel = Babel(app)


class Config(object):
    """configuration for babel."""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """Render 4-index.html template."""
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    """Check the URL parameter for locale variable and force it  on app."""
    if request.args.get('locale'):
        lang = request.args.get('locale')
        if lang in app.config['LANGUAGES']:
            return lang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
