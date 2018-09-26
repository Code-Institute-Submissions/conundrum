import os
from random import randint
from flask import Flask, render_template, redirect, request, url_for, session
import os.path


app = Flask(__name__)
app.secret_key = os.urandom(24)


# function to write or append to files
def write_file(file_name, file_type, data):
    with open(file_name, file_type) as file:
        file.writelines(data)
        return file


# function to read files
def read_file(file_name):
    with open(file_name, "r" ) as file:
        lines = file.read().splitlines()
        return lines


# Counts the number of questions in questions.txt.
def number_of_questions():
    number = read_file("data/questions.txt")
    return len(number)-2


# Counts the number of incorrect answers in incorrect_answers.txt
def number_of_incorrect_answers(username):
    lines = read_file("data/incorrect_answers_" + username + ".txt")
    return len(lines)


# Counts the number of incorrect answers in leaderboard.txt
def number_of_lines_in_leaderboard():
    lines = read_file("data/leaderboard.txt")
    return len(lines)


# For displaying the number of remaining guesse
def remaining_guesses(username):
    return 10 - number_of_incorrect_answers(username)


# reads the lines in questions.txt
def read_questions():
    questions = read_file("data/questions.txt")
    return questions


# reads the lines in answers.txt
def read_answers():
    answers = read_file("data/answers.txt")
    return answers


# Reads the answer.txt. the answers are determined by the page number.
# used in conundrum.html to show that the user got the correct answer.
def change_answer(page_number):
    answer = read_answers()[-1 + page_number]
    return answer.capitalize()


# Reads the question.txt. Changes the question when the page number increases.
def change_question(page_number):
    return read_questions()[0 + page_number]


# Reads the answer.txt. the answers are determined by the page number.
# The answer changes when the page_number increase.
def correct_answer(page_number):
    return read_answers()[0 + page_number]


# Writes the users incorrect answer to their incorrect answer file.
def write_incorrect_answer(username):
    return write_file("data/incorrect_answers_" + username + ".txt", "a", request.form["answer"].capitalize() + "\n")


# Reads the users incorrect answers.
def read_incorrect_answers(username):
    return read_file("data/incorrect_answers_" + username + ".txt")


# Creates a form for the users incorrect answers.
def create_incorrect_answer_form(username):
    with open("data/incorrect_answers_" + username + ".txt", "a+") as file:
        incorrect_answers = file.read().splitlines()
        return incorrect_answers


# If the user enters nothing in the input field, this returns a string.
def empty_user_form():
    empty = "A username is required to play."
    return empty


# returns the question number, and number of questions displayed on the conundrum.html
def question_number(page_number):
    return "Question {0} of {1}".format(page_number + 1, number_of_questions()+1)


# This records the username and their final score to the leaderboard file.
def final_score(username, score):
    if score < 10:
        score = write_file("data/leaderboard.txt", "a", username + "\n" + "  " + str(score) + "\n")
        return score
    elif score > 99:
        score = write_file("data/leaderboard.txt", "a", username + "\n" +  str(score) + "\n")
        return score
    else:
        score = write_file("data/leaderboard.txt", "a", username + "\n" + " " + str(score) + "\n")
        return score


# For the leaderboard when sorting the top ten score, this sorts the second index postion. Called in leader_results().
def sort_score(x):
    return x[1]


# This reads the score and username from the leaderboard.txt file. Sorts the pairs into a dictionary and then sorts them by score order from highest to lowest.
def leader_results():
    lines = read_file("data/leaderboard.txt")
    name = []
    score = []
    for i, text in enumerate(lines):
        if i % 2 == 0:
            name.append(text)
        else:
            score.append(text)
    name_and_score = zip(name, score)

    result = sorted(name_and_score, key=sort_score, reverse=True)
    return result
print(leader_results())

# Shows the individual users score on the leaderboard screen.
def leaderboard_final_score():
    lines = read_file("data/leaderboard.txt")
    return lines


# This clears the incorrect answers from the users file.
def clear_Incorrect_answers(username):
    write_file("data/incorrect_answers_" + username + ".txt", "w", "")


# Index Page
@app.route('/', methods=["GET", "POST"])
def index():

    session['score'] = 0
    session['page_number'] = 0
    session['positive_negative_points'] = 0

    if request.method == "POST":
        # If the username field is empty, redirect to the same page and return a string, empty = "A username is required to play.".
        if request.form["username"] == "":
            return render_template("index.html", empty=empty_user_form())

        else:
            # Creates a new file for the user in their name. Clears any answers before entering in case a user with the same name already created a file.
            # Redirect to the conundrum page
            session['username'] = request.form['username']
            user = session['username']
            create_incorrect_answer_form(user)
            clear_Incorrect_answers(user)
            return redirect(url_for('conundrum', username=user))

    return render_template("index.html")

# Questions and answers page----------------------------------------------------


@app.route('/conundrum/<username>', methods=["GET", "POST"])
def conundrum(username):

    score = session['score']
    page_number = session['page_number']
    positive_negative_points = session["positive_negative_points"]

    userfile = "data/incorrect_answers_" + username + ".txt"  # goes with os.remove(userfile) to delete the user file when the leaderboard is reached.

    if os.path.exists(userfile):
        # If a user file exists continue. Used to prevent cheating.
        if request.method == "POST":

            if request.form["answer"].lower() == correct_answer(page_number) and not 'skip' in request.form:
                # If the answer entered into the answer input box is the same as in the index position of answers.txt. Clear the user incorrect answers file
                clear_Incorrect_answers(username)

                if page_number < number_of_questions():
                    # If the page number(question number) is less than the total amount of questions, add the positive scores and increase the page number
                    # so the question changes. redirect to the same page
                    session['score'] += 10
                    session['page_number'] += 1
                    session["positive_negative_points"] = 0
                    return redirect(url_for('conundrum', username=username))

                else:
                    # If the page number(question number) is equal to the total amount of questions, add the positive scores write to the leaderboard file and
                    # redirect to the leaderboard page. Final_score writes to the leaderboard.txt file
                    score = score + 10
                    final_score(username, score)
                    os.remove(userfile)
                    return redirect(url_for('leaderboard', username=username))

            elif 'skip' in request.form or number_of_incorrect_answers(username) == 9:
                # If the skip botton is pressed or the user has had 9 incorrect answers, clear the incorrect answers
                clear_Incorrect_answers(username)

                if page_number < number_of_questions():
                    # If the page number(question number) is less than the total amount of questions. Add negative scores and increase the page number
                    # so the question changes. redirect to the same page.
                    session['score'] -= 2
                    session['page_number'] += 1
                    session["positive_negative_points"] = 2
                    return redirect(url_for('conundrum', username=username))

                else:
                    # If the page number(question number) is equal to the total amount of questions, take the negative scores, write to the leaderboard file and
                    # redirect to the leaderboard page.
                    score = score - 2
                    final_score(username, score)
                    os.remove(userfile)
                    return redirect(url_for('leaderboard', username=username))

            elif request.form["answer"] == "":
                # if the input field is empty, redirect to the same page.
                return redirect(url_for('conundrum', username=username))

            elif request.form["answer"].lower() != correct_answer(page_number):
                # If the guess is not equal to the answer. Take negative points, write the incorrect answer to the users incorrect answer form and redirect to the
                # same page.
                session['score'] -= 1
                session["positive_negative_points"] = 1

                write_incorrect_answer(username)  # Writes the incorrect answers to the users incorrect answer file.
                return redirect(url_for('conundrum', username=username))
    else:
        return redirect(url_for('index'))
    return render_template("conundrum.html", score=score,
                                             userfile=userfile,
                                             username=username,
                                             page_number=page_number,
                                             answer=change_answer(page_number),
                                             question=change_question(page_number),
                                             question_num=question_number(page_number),
                                             incorrect=read_incorrect_answers(username),
                                             guesses_remaining=remaining_guesses(username),
                                             positive_negative_points=positive_negative_points)

# Leaderboard ------------------------------------------------------------------


@app.route('/conundrum/leaderboard/<username>')
def leaderboard(username):
    # prints out the leaderboard scores and usernames
    results = leader_results()
    return render_template("leaderboard.html", results=results,
                                                user_final_score=leaderboard_final_score(),
                                                username=username,
                                                number_in_leaderboard=number_of_lines_in_leaderboard(),
                                                total_points=(number_of_questions() + 1) * 10)
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
