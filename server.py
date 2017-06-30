"""Flask server for code website."""

from jinja2 import StrictUndefined

from flask import Flask, session, flash, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

# import classes from model module
from model import User, Level, Module, Function

# import database necessities from model module
from model import db, connect_to_db


app = Flask(__name__)

# necessary for using Flask sessions and debug toolbar
app.secret_key = "code"

# forces an error to be raised if variable is undefined in Jinja2
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def show_homepage():
    """Display homepage"""

    flash(session)

    return render_template("homepage.html")


@app.route("/register", methods=['GET'])
def show_register_form():
    """Displays registration form."""

    return render_template("register.html")


@app.route("/register", methods=['POST'])
def register_user():
    """Registers user."""

    username = request.form.get("username")
    password = request.form.get("password")
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    email = request.form.get("email")

    if User.query.filter_by(username=username).all():
        flash("Username is already in use. Please choose a different one.")
    else:
        user = User(username=username, 
                    password=password, 
                    first_name=first_name, 
                    last_name=last_name, 
                    email=email)

        db.session.add(user)
        db.session.commit()

        flash("You have registered as {}.".format(username))

    return render_template("homepage.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Login user"""

    if request.method == "GET":

        return render_template("login.html")

    elif request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if User.query.filter_by(username=username, password=password).first():
            session["current_user"] = username
            flash("Welcome. You are logged in as {}".format(username))
        else:
            flash("Username or password does not match. Please try again.")

        return redirect("/<username>/dashboard")


@app.route("/logout")
def logout():
    """Logout user"""

    if "current_user" in session:
        del session["current_user"]

    flash("You are logged out.")
    return redirect("/")


@app.route("/<username>/dashboard")
def show_dashboard(username):
    """Show student dashboard"""

    return render_template("dashboard.html")



if __name__ == "__main__":

    # for debugging
    app.debug = True

    connect_to_db(app)

    # Use DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
