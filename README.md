PyQuizBase: A Python Study Tool
===============================

This is a program created for coding students that allows them to store notes in a database and uses those entries in a quiz to test the students' knowledge.

Tech Stack:
-----------
Python, Flask, Jinja, Javascript, jQuery, HTML, CSS, Bootstrap, SQL, SQLAlchemy, PostgreSQL

![Homepage](/static/img/Homepage.png)

Features
--------

Registration/Login

Students can create their own personalized account and log in to the program. The student data is saved in a user table in the PostgreSQL database. The login works by saving the user info to a Flask session on login and by verification before pages can be accessed.

Dashboard

The dashboard contains buttons that link to different parts of the program and can easily be returned to from other pages.

![Dashboard](/static/img/Dashboard.png)

Study Notes Database

There are modules/functions tables in the PostgreSQL database, which contains all the students' notes along with some starter sample data. Students are able to add new modules and associated functions. The data displays as an interactive Bootstrap table. When a module is clicked on, SQLAlchemy relationships are used so that functions associated with the module id are displayed and hidden as a subtable using a jQuery functionality on click.

![Study Notes Table](/static/img/Study_Notes_Table.png)

Quiz

The quiz randomly queries an entry from the database along with additional entries of the same type as answers and puts them in a jinja template to display multiple choice questions for students to answer. The information is also saved in a Flask session. After answering the question, students are redirected to an answer page that tells them the results. If the answer matches what is saved in the session, the progress bar will also show an increase.

Progress

There is an entry in the database that increments as students answer questions correctly. This is used to calculate a student's level along with a percentage for a progress bar that displays how close they are to levelling up.

![Quiz](/static/img/Quiz.png)