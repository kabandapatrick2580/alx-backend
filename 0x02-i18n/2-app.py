#!/usr/bin/env python3
"""Basic Flask setup."""

from flask import Flask, render_template, request
from flask_babel import Babel

# Initialize a Flask app.
app = Flask(__name__)


class Config(object):
    """Configure Babel."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

# Instantiate the Babel object.
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine best language match based on supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Home page of our Flask application."""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
