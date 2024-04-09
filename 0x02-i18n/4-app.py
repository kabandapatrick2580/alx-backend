#!/usr/bin/env python3
"""Basic Flask setup."""
from flask import Flask, render_template, request, g
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
    Determine the best language match based on supported languages.

    If the 'locale' parameter is present in the request URL and is supported,
    it returns the requested locale. Otherwise, it resorts to the default
    behavior and selects the best match from the accepted languages.
    """
    if 'locale' in request.args:
        requested_locale = request.args.get('locale')
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """Home page of our Flask application."""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
