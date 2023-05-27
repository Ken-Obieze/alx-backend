#!/usr/bin/env python3
"""
Module for Flask app with Babel setup, locale selection, parametrized templates,
URL parameter support for locale, mock user login system, user locale priority,
and inference of appropriate time zone
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
import pytz
from datetime import datetime
from flask_babel import format_datetime

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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """
    Get the user dictionary based on the user ID
    Returns None if the user ID cannot be found or if login_as was not passed
    """
    return users.get(user_id)


@babel.localeselector
def get_locale():
    """
    Determine the best match for the supported languages based on the user's preferred locale,
    request's Accept-Language header, or default locale
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    Determine the best match for the supported time zones based on the user's preferred time zone,
    user settings, or default to UTC
    """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.UnknownTimeZoneError:
            pass
    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.before_request
def before_request():
    """
    Executed before all other functions
    Finds the user if any based on the login_as URL parameter and sets it as a global on flask.g.user
    """
    user_id = request.args.get('login_as')
    if user_id:
        user = get_user(int(user_id))
        g.user = user


@app.route('/')
def index():
    """
    Renders the index.html template with appropriate welcome message based on the logged-in user
    """
    if g.user:
        welcome_message = gettext('logged_in_as') % {'username': g.user['name']}
    else:
        welcome_message = gettext('not_logged_in')
    
    current_time = datetime.now(pytz.timezone(g.timezone))
    formatted_time = format_datetime(current_time)
    
    return render_template('7-index.html', welcome_message=welcome_message, current_time=formatted_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='500
