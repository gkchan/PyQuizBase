"""Database functions for coding tool project."""

from flask_sqlalchemy import SQLAlchemy

# This connects to a PostgreSQL database and uses the Flask-SQLAlchemy library.

db = SQLAlchemy()

# Model definitions.



# NOTE: add backref



class User(db.Model):
    """Creates a table for user info."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)


class Level(db.Model):
    """Creates a table for tracking user progress."""

    __tablename__ = "levels"

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    level = db.Column(db.Integer, nullable=False, default=0)
    points = db.Column(db.Integer, nullable=False, default=0)


class Module(db.Model):
    """Creates a table of modules."""

    __tablename__ = "modules"

    module_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    additional_info = db.Column(db.Text, nullable=True)


class Functions(db.Model):
    """Creates a table for functions."""

    __tablename__ = "functions"

    function_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    additional_info = db.Column(db.Text, nullable=True)





