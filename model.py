"""Database functions for coding tool project."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# This connects to a PostgreSQL database and uses the Flask-SQLAlchemy library.

db = SQLAlchemy()

# Model definitions.

class User(db.Model):
    """Creates a table for user info."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False, unique=True)

    levels = db.relationship("Level", uselist=False, backref="users")
    modules = db.relationship("Module", backref="users")
    functions = db.relationship("Function", backref="users")

    def __repr__(self):
        """Show info about user."""

        return "< User id={}, username={}, email={} >".format(self.user_id, self.username, self.email)


class Level(db.Model):
    """Creates a table for tracking user progress."""

    __tablename__ = "levels"

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    level = db.Column(db.Integer, nullable=False, default=0)
    points = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        """Show info about level."""

        return "< User id={}, level={}, points={} >".format(self.user_id, self.level, self.points)


class Module(db.Model):
    """Creates a table of modules."""

    __tablename__ = "modules"

    module_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    additional_info = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    functions = db.relationship("Function", backref="modules")

    def __repr__(self):
        """Show info about modules."""

        return "< Module id={}, name={}>".format(self.module_id, self.name)


class Function(db.Model):
    """Creates a table for functions."""

    __tablename__ = "functions"

    function_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    additional_info = db.Column(db.Text, nullable=True)
    sample_code = db.Column(db.String(256), nullable=True)
    output = db.Column(db.String(256), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    module_id = db.Column(db.Integer, db.ForeignKey("modules.module_id"),
                 nullable=False, default=2) # default will be unavailable in finished version if no module is put in 

    def __repr__(self):
        """Show info about functions."""

        return "< Function id={}, name={}>".format(self.function_id, self.name)


#Helper functions

def connect_to_db(app):
    """Connects the database to Flask app"""

    #Configure for use with our PostgreSQL database.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///code'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    #Allows database to be run interactively when file is run.

    from server import app
    connect_to_db(app)
    print "Connected to DB."


