"""Utility file to seed code database with seed data."""

# import classes from model module
from model import User, Level, Module, Function

# import database necessities from model module
from model import db, connect_to_db

def load_users():
    """Load seed_user into database."""

    print "Users"

    # delete users before data gets added to avoid duplicate info
    User.query.delete()

    # insert data from seed_user
    with open("seed_data/seed_user") as user_data:
        for row in user_data:
            print user_data
            username, first_name, last_name, email = row.rstrip().split("|")

            user = User(username=username, first_name=first_name, last_name=last_name, email=email)

            # add user to session     
            db.session.add(user)

    # commit changes
    db.session.commit()

    print "Users loaded."




