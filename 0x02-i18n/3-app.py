#!/usr/bin/env python3
"""Flask app Module with Babel, locale selection, parametrized templates."""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__, static_url_path='')
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
    """Determine the best match for the supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """Render the index.html template with parametrized values."""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
