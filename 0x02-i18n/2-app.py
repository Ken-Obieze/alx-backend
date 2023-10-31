#!/usr/bin/env python3
"""Module for Flask app with Babel setup and locale selection."""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class for Flask app."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel.init_app(app)


@babel.localeselector
def get_locale():
    """Best match for supported languages based on  Accept-Language header"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Renders the index.html template."""
    return render_template('2-index.html', \
        title=gettext('Welcome to Holberton'), \
        header=gettext('Hello world'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
