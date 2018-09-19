import os 
from flask import Flask, render_template, redirect, request, url_for
import requests
from multiprocessing import Value

app = Flask(__name__)

# function to write or append to files
def write_file(file_name, file_type, data):
    with open(file_name, file_type) as file:
        file.writelines(data)
        return file
        
# function to read files
def read_file(file_name):
    with open(file_name, "r") as file:
        lines = file.read().splitlines()
        return lines

# Counts the number of questions in questions.txt. Used to make a score or which question you're up to.
def number_of_questions():
    number = read_file("data/questions.txt")
    return len(number)-2
        
#Changes the question when the counter increases        
def change_question(page_number):
    questions = read_file("data/questions.txt")
    return questions[0 + page_number]

def write_incorrect_answer(username):
    file = write_file("data/incorrect_answers_" + username +".txt", "a", request.form["answer"] + "\n")
    return file
    
def read_incorrect_answers(username):
    with open("data/incorrect_answers_" + username +".txt", "r") as file:
        lines = file.read().splitlines()
        return lines
        
def incorrect_answer_length(username):
    lines = read_file("data/incorrect_answers_" + username +".txt")
    return len(lines)

def create_incorrect__answer_form(username):
    with open("data/incorrect_answers_" + username +".txt", "a+") as file:
        lines = file.read().splitlines()
        return lines

def empty_form():
    empty = "A username is required to play."
    return empty
    
def skip_final_score(username, score):
    return write_file("data/leaderboard.txt", "a", "{0} {1}".format(username, score))
    
# returns the question number, and number of questions displayed on the conundrum.html  
def question_number(page_number):
    return "Question {0} of {1}".format(page_number + 1 , number_of_questions()+1)
    
def final_score(score):
    return "\n{0}".format(score)
    
def remaining_guesses(username):
    remaining = 10 - incorrect_answer_length(username)
    return remaining

def leader_results():
    with open("data/leaderboard.txt", "r") as file:
        lines = file.read().splitlines() 
        name = []
        score = []
        for i, text in enumerate(lines):
            if i%2 ==0:
                name.append(text)
            else:
                score.append(text)
        name_and_score = zip(name,score)
       
        result = sorted(name_and_score, reverse=True)
        print(result)
        return result
        
def clear_answers(username):
    write_file("data/incorrect_answers_" + username +".txt", "w", "")

# Index Page--------------------------------------------------------------------
@app.route('/', methods=["GET", "POST"])
def index():
    page_number = 0
    score = 0
    empty = empty_form()
    if request.method == "POST":
        if request.form["username"] == "":
            return render_template("index.html", empty = empty)
        
        else:
            create_incorrect__answer_form(request.form["username"])
            clear_answers(request.form["username"])
            return redirect(url_for('conundrum', username = request.form['username'], page_number = page_number, score = score ))
        
    return render_template("index.html")

# Questions and answers page----------------------------------------------------

@app.route('/conundrum/<username>/<int:page_number>/<int:score>', methods=["GET", "POST"])    

def conundrum(username, page_number, score):
    #This opens up a user named file for the users incorrect answers. created so other user incorrect answers don't add to another user. 
    
    userfile = "data/incorrect_answers_" + username +".txt"
    if request.method == "POST":
        
        if page_number == number_of_questions():
            answers = read_file("data/answers.txt")
            
            for answer in (answers):
                
                if request.form["answer"] == answers[0 + page_number] and not 'skip' in request.form:
                    # Each time the question is answered correctly, os.remove(userfile) will delete the txt.file.
                    score = score + 10
                    clear_answers(username)
                    write_file("data/leaderboard.txt", "a", username + final_score(score) +"\n")
                    return redirect(url_for('leaderboard', username = username, page_number = page_number + 1, score = score))
                    
                elif 'skip' in request.form or incorrect_answer_length(username) == 9:
                    if score == 0:
                        score = 0
                    else:
                        score = score -2
                    clear_answers(username)
                    write_file("data/leaderboard.txt", "a", username + final_score(score) +"\n")
                    return redirect(url_for('leaderboard', username = username, page_number = page_number + 1, score = score))
                    
                elif request.form["answer"] == "":
                    return redirect(url_for('conundrum', username = username, page_number = page_number, score = score))
                    
                elif request.form["answer"] != answers[0 + page_number]:
                    if score == 0:
                        score = 0
                    else:
                        score = score -1
                    write_incorrect_answer(username)
                    return redirect(url_for('conundrum', username = username, page_number = page_number, score = score))
                
        
        elif page_number < number_of_questions():
            
            answers = read_file("data/answers.txt")
                
            for answer in (answers):
                
                if request.form["answer"] == answers[0 + page_number] and not 'skip' in request.form:
                    clear_answers(username)
                    
                    return redirect(url_for('conundrum', username = username, page_number = page_number + 1, score = score + 10))
                    
                elif 'skip' in request.form or incorrect_answer_length(username) == 9:
                    if score == 0:
                        score = 0
                    else:
                        score = score -2
                    clear_answers(username)
                    return redirect(url_for('conundrum', username = username, page_number = page_number + 1, score = score)) 
                    
                elif request.form["answer"] == "":
                    return redirect(url_for('conundrum', username = username, page_number = page_number, score = score))
                    
                elif request.form["answer"] != answers[0 + page_number]:
                    if score == 0:
                        score = 0
                    else:
                        score = score -1
                    write_incorrect_answer(username)
                    return redirect(url_for('conundrum', username = username, page_number = page_number, score = score))
    
    return render_template("conundrum.html", question = change_question(page_number), question_num = question_number(page_number), 
                                            page_number = page_number, username = username, 
                                            score = score, incorrect = read_incorrect_answers(username), userfile= userfile, guesses_remaining = remaining_guesses(username))
    
# Leaderboard ------------------------------------------------------------------
@app.route('/conundrum/leaderboard/<username>/<int:page_number>/<int:score>')
def leaderboard(username, page_number, score):
    
    results = leader_results()
    
    
    return render_template("leaderboard.html", results = results, username = username, page_number = page_number, score = score, total_points = (number_of_questions() + 1) * 10)
if __name__ == '__main__':
    app.run(host=os.getenv('IP'),port=int(os.getenv('PORT')),debug=True)
