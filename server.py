"""Flask server for code website."""

from jinja2 import StrictUndefined

from flask import Flask, session, flash, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

# import classes from model module
from model import User, Level, Module, Function

# import database necessities from model module
from model import db, connect_to_db

from questions import ask_question


app = Flask(__name__)

# necessary for using Flask sessions and debug toolbar
app.secret_key = "code"

# forces an error to be raised if variable is undefined in Jinja2
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def show_homepage():
    """Display homepage"""

    # for developing/testing purposes:
    print session

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

        return redirect("/{}/dashboard".format(username))


@app.route("/logout")
def logout():
    """Logout user"""

    if "current_user" in session:
        del session["current_user"]

    flash("You are logged out.")
    return redirect("/")


def verify_user(username):
    """Verify user login"""

    if ("current_user" in session and session["current_user"] == username) == False:
        flash("Please login.")
        return redirect("/login")
   

@app.route("/<username>/dashboard")
def show_dashboard(username):
    """Show student dashboard"""

    verify_user(username)
    
    return render_template("dashboard.html", username=session["current_user"])


@app.route("/<username>/info")
def show_user_info(username):
    """Show user info"""

    verify_user(username)

    user = User.query.filter_by(username=username).first()
    return render_template("user_info.html",
                            user=user)


@app.route("/<username>/studynotes")
def show_study_notes(username):
    """Show study notes"""

    # verify_user(username)

    study_table = db.session.query(Module).all()
        
    return render_template("study_notes.html", 
                            study_table=study_table, 
                            username=username)


@app.route("/<username>/addmodules", methods=["GET", "POST"])
def add_modules(username):
    """Add function/module information"""

    # currently only handles basic adding of info

    # verify_user(username)

    if request.method == "GET":

        return render_template("add_modules.html", username=username)

    elif request.method == "POST":

        mname = request.form.get("mname")
        mdesc = request.form.get("mdesc")
        fname = request.form.get("fname")
        fdesc = request.form.get("fdesc")
        samplecode = request.form.get("samplecode")
        output = request.form.get("output")

        # fetch user to get user_id
        user = User.query.filter_by(username=username).first()

        module = Module(name=mname,
                        description=mdesc,
                        user_id=user.user_id)

        db.session.add(module)

        # fetch module to get module_id
        module = Module.query.filter_by(name=mname,
                                        description=mdesc,
                                        user_id=user.user_id).first()

        function = Function(name=fname, 
                            description=fdesc, 
                            sample_code=samplecode, 
                            output=output,
                            user_id=user.user_id,
                            module_id=module.module_id)

        db.session.add(function)
        db.session.commit()

        flash("Your notes have been added.")

        return redirect("/{}/studynotes".format(username))


@app.route("/quiz", methods=["GET", "POST"])
def display_question():
    """Displays question to answer and then displays results with answer."""

    # chooses a function entry and asks a question
    question, input_code, answer, answer_choices = ask_question()

    if request.method == "GET":

        return render_template("question.html", 
                                question=question, 
                                input_code=input_code, 
                                answer=answer,
                                answer_choices=answer_choices)

    elif request.method == "POST":

        user_answer = request.form.get("useranswer")
        if user_answer == answer:
            result = "correct!"
        else:
            result = "wrong. Don't gve up. Keep studying, and you'll get it right next time!"

        return render_template("answer.html", result=result, answer=answer)

    else:
        flash("That is an invalid method.")








                      
 
        









if __name__ == "__main__":

    # for debugging
    app.debug = True

    connect_to_db(app)

    # Use DebugToolbar
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')
