# Questions for quiz in learning code program

# More questions to come depending on time

# import classes from model module
from model import User, Level, Module, Function

# import database necessities from model module
# from model import db, connect_to_db

from random import randint, sample


# May have separate or combined functions depending on what program ultimately does

# def choose_random_function():
#     "Chooses a random function entry from the database"

#     function_count = Function.query.count()
#     function_id = randint(1, function_count)
#     function_entry = Function.query.get(function_id)

#     # simple testing/debugging during development
#     print function_count, function_id, function_entry

#     return function_entry


def ask_question():
    """Asks a question about the sample code and output"""
    
    function_count = Function.query.count()
    function_id = randint(1, function_count)
    function_entry = Function.query.get(function_id)

    # simple testing/debugging during development
    print function_count, function_id, function_entry

    # template not showing new line this way:
    # sample_code_question = "What output do you get when you input the following code?\n" + function_entry.sample_code

    sample_code_question = "What output do you get when you input the following code?"
    sample_code = function_entry.sample_code

    answer = function_entry.output

    # simple testing/debugging during development
    print sample_code_question, answer

    return sample_code_question, sample_code


