import os 
from flask import Flask, render_template, redirect, request

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

#This keeps the count of how many lines are in the count.txt    
def counter():
    with open("data/count.txt", "r") as file:
        count = file.readlines()
        count = len(count)
        print(count)
        return count
        
def reset_counter():
    if counter() == number_of_questions():
        write_file("data/count.txt", "w", "")
# Counts the number of questions in questions.txt

def number_of_questions():
    number = read_file("data/questions.txt")
    return len(number)-1
    
# returns the question number, and number of questions displayed on the conundrum.html  
def question_number():
    return "Question {0} of {1}".format(counter()+ 1 , number_of_questions())
    
def final_score():
    return ": {0} out of {1}".format(counter() , number_of_questions())
        
#Changes the question when the counter increases        
def change_question():
    questions = read_file("data/questions.txt")
    return questions[0 + counter()]
    
def leader_results():
    with open("data/leaderboard.txt", "r") as file:
        result = file.readlines()
        
        return result

# This reads from answers.txt. If the form input is equal to the answers.txt answer, the count will increase by one.
def get_answers(username):
        answers = read_file("data/answers.txt")
        
        for answer in (answers):
            
            if request.method == "POST":
                if request.form["answer"] == answers[0 + counter()]:
                    
                    write_file("data/count.txt", "a", "1\n")
            
            return len(answers)

        
            
# Index Page--------------------------------------------------------------------
@app.route('/', methods=["GET", "POST"])
def index():
    
    if request.method == "POST":
        
        return redirect("conundrum/" + request.form["username"])
        
    return render_template("index.html")
    

# Questions and answers page----------------------------------------------------
@app.route('/conundrum/<username>', methods=["GET", "POST"])    

def conundrum(username):
    counter()
    
    get_answers(username)
    data = change_question()
    question_num = question_number()
    if counter() == number_of_questions():
        if request.method == "POST":
            write_file("data/leaderboard.txt", "a", username + final_score() +"\n")
            return redirect('/conundrum/leaderboard/' + username)
    elif counter() < number_of_questions(): 
        
        if request.method == "POST":
            return redirect("conundrum/" + username)
            
    return render_template("conundrum.html", data = data, question_num = question_num)
    
    
# Leaderboard ------------------------------------------------------------------
@app.route('/conundrum/leaderboard/<username>')
def leaderboard(username):
    results = leader_results()
    
    reset_counter()
    num = final_score()
    return render_template("leaderboard.html", results = results)
    

app.run(host=os.getenv('IP'),port=int(os.getenv('PORT')),debug=True)
