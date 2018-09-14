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

#this reads the number of lines in this file     
def counter():
    with open("data/count.txt", "r") as file:
        count = file.readlines()
        count = len(count)
        return count
        
#Changes the question when the counter increases        
def change_question():
    questions = read_file("data/questions.txt")
    return questions[0 + counter()]

# This will read from the answers file. If the form input answer is equal to the text file answer, the count will increase by one.
def get_answers():
        answers = read_file("data/answers.txt")
        
        for answer in (answers):
            if counter() < len(answers)-1:
                if request.method == "POST":
                    if request.form["answer"] == answers[0 + counter()]:
                        write_file("data/count.txt", "a", "1\n")
            else:
                if request.method == "POST":
                    if request.form["answer"] == answers[0 + counter()]:
                        write_file("data/count.txt", "w", "")

# Index Page
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect("conundrum/" + request.form["username"])
        
    return render_template("index.html")

# Questions and answers page
@app.route('/conundrum/<username>', methods=["GET", "POST"])    

def conundrum(username):
    get_answers()
    data = change_question()
    if request.method == "POST":
        return redirect("conundrum/" + username)
    
    return render_template("conundrum.html", data = data)

app.run(host=os.getenv('IP'),port=int(os.getenv('PORT')),debug=True)