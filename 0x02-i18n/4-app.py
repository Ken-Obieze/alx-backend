#!/usr/bin/env python3
"""
Module for Flask app with Babel setup, locale selection, parametrized templates, and URL parameter support for locale
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class for Flask app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel.init_app(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match for the supported languages based on the request's Accept-Language header
    If a 'locale' parameter is present in the URL and it is a supported locale, return it
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Renders the index.html template with parametrized values
    """
    return render_template('4-index.html', title=gettext('home_title'), header=gettext('home_header'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
