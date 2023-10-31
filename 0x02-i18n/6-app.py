#!/usr/bin/env python3
"""Module For Flask app."""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

app.config['LANGUAGES'] = ['en', 'fr']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """Retrieve a user from the mock user database based on the user ID."""
    return users.get(user_id)


@babel.localeselector
def get_locale():
    """
    Determines the best matching locale for the request.
    Priority:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    user = get_user(g.user_id)
    if user and user['locale'] in app.config['LANGUAGES']:
        return user['locale']
    locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if locale:
        return locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.before_request
def before_request():
    """Execute before other functions."""
    user_id = request.args.get('login_as')
    g.user_id = int(user_id) if user_id else None
    g.user = get_user(g.user_id)


@app.route('/')
def index():
    """Render index.html template with appropriate welcome message."""
    welcome_message = ''
    if g.user:
        welcome_message = f"You are logged in as {g.user['name']}."
    else:
        welcome_message = "You are not logged in."

    return render_template('6-index.html', welcome_message=welcome_message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
