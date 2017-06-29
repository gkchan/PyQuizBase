"""Flask server for code website."""

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

# import classes from model module
from model import User, Level, Module, Function

# import database necessities from model module
from model import db, connect_to_db


app = Flask(__name__)

# necessary for using Flask sessions and debug toolbar
app.secret_key = "code"




if __name__ == "__main__":

    # for debugging
    app.debug = True

    connect_to_db(app)

    # Use DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
