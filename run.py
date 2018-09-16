import os 
from flask import Flask, render_template, redirect, request, url_for
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

def write_incorrect_answer():
    file = write_file("data/incorrect_answers.txt", "a", request.form["answer"] + "\n")
    return file
    
def incorrect_answer():
    with open("data/incorrect_answers.txt", "r") as file:
        lines = file.read().splitlines()
        return lines
        
def clear_answers():
    write_file("data/incorrect_answers.txt", "w", "")

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
            return redirect(url_for('conundrum', username = request.form['username'], page_number = page_number, score = score ))
        
    return render_template("index.html")

# Questions and answers page----------------------------------------------------

@app.route('/conundrum/<username>/<int:page_number>/<int:score>', methods=["GET", "POST"])    

def conundrum(username, page_number, score):
    skip = page_number + 1
    
    question = change_question(page_number)
    question_num = question_number(page_number) 
    incorrect = incorrect_answer()
    if request.method == "POST":
        
        if page_number == number_of_questions():
                answers = read_file("data/answers.txt")
                
                for answer in (answers):
                    
                    if request.form["answer"] == answers[0 + page_number]:
                        page_number = page_number + 1
                        score = score + 10
                        clear_answers()
                        return redirect(url_for('leaderboard', username = username, page_number = page_number, score = score))
                    
                    else:
                        
                        return redirect(url_for('conundrum', username = username, page_number = page_number, score = score))
        
        elif page_number < number_of_questions():
            
                answers = read_file("data/answers.txt")
                
                for answer in (answers):
                    
                    if request.form["answer"] == answers[0 + page_number]:
                        page_number = page_number + 1
                        score = score + 10
                        clear_answers()                
                        return redirect(url_for('conundrum', username = username, page_number = page_number, score = score))
                    else:
                        write_incorrect_answer()
                        return redirect(url_for('conundrum', username = username, page_number = page_number, score = score))  
        
            
    return render_template("conundrum.html", question = question, question_num = question_num, 
                                            page_number = page_number, username = username, skip = skip, 
                                            score = score, incorrect = incorrect)
    
# Leaderboard ------------------------------------------------------------------
@app.route('/conundrum/leaderboard/<username>/<int:page_number>/<int:score>')
def leaderboard(username, page_number, score):
    write_file("data/leaderboard.txt", "a", username + final_score(score) +"\n")
    results = leader_results()
    
    
    return render_template("leaderboard.html", results = results, score = score)

app.run(host=os.getenv('IP'),port=int(os.getenv('PORT')),debug=True)
