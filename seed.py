"""Utility file to seed code database with seed data."""

# import classes from model module
from model import User, Level, Module, Function

# import database necessities from model module
from model import db, connect_to_db


from flask import Flask
app = Flask(__name__)


def load_users():
    """Load user data into database."""

    print "Users"

    # delete users before data gets added to avoid duplicate info
    # User.query.delete()

    # insert data from seed_user
    with open("seed_data/seed_user") as user_data:
        for row in user_data:
            username, password, first_name, last_name, email = row.rstrip().split("|")
            user = User(username=username, 
                        password=password, 
                        first_name=first_name, 
                        last_name=last_name, 
                        email=email)

            # add user to session     
            db.session.add(user)

    # commit changes
    db.session.commit()

    print "Users loaded."


def load_levels():
    """Load level data to database."""

    print "Levels"

    # delete levels before data gets added to avoid duplicate info
    # Level.query.delete()

    # insert data from seed_level
    with open("seed_data/seed_level") as level_data:
        for row in level_data:
            user_id, level, points = row.rstrip().split("|")
            level = Level(user_id=user_id, level=level, points=points)

            # add level to session     
            db.session.add(level)

    # commit changes
    db.session.commit()

    print "Levels loaded."


def load_modules():
    """Load modules data to database."""

    print "Modules"

    # delete modules before data gets added to avoid duplicate info
    # Module.query.delete()

    # insert data from seed_module
    with open("seed_data/seed_module") as module_data:
        for row in module_data:
            name, description, additional_info, user_id = row.rstrip().split("|")
            module = Module(name=name, description=description, additional_info=additional_info, user_id=user_id)

            # add module to session     
            db.session.add(module)

    # commit changes
    db.session.commit()

    print "Modules loaded."


def load_functions():
    """Load functions data to database."""

    print "Functions"

    # delete modules before data gets added to avoid duplicate info
    # Function.query.delete()

    # insert data from seed_function
    with open("seed_data/seed_function") as function_data:
        for row in function_data:
            name, description, additional_info, sample_code, output, user_id, module_id = row.rstrip().split("|")
            function = Function(name=name, 
                                description=description, 
                                additional_info=additional_info, 
                                sample_code=sample_code, 
                                output=output,
                                user_id=user_id,
                                module_id=module_id)

            # add function to session     
            db.session.add(function)

    # commit changes
    db.session.commit()

    print "Function loaded."


if __name__ == "__main__":

    connect_to_db(app)

    # Create tables if not created
    db.create_all()

    # Load data
    load_users()
    load_levels()
    load_modules()
    load_functions()


