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
    
#Counts the number of lines in the users incorrect answers form
def number_of_incorrect_answers(username):
    lines = read_file("data/incorrect_answers_" + username +".txt")
    return len(lines)
    
# Determines the remaining amount of guesses  
def remaining_guesses(username):
    return 10 - number_of_incorrect_answers(username)
        
# Changes the question when the page number increases.       
def change_question(page_number):
    questions = read_file("data/questions.txt")
    return questions[0 + page_number]

# Writes the users incorrect answer to their incorrect answer file.
def write_incorrect_answer(username):
    return write_file("data/incorrect_answers_" + username +".txt", "a", request.form["answer"] + "\n")
     
# Reads the users incorrect answers. 
def read_incorrect_answers(username):
    return read_file("data/incorrect_answers_" + username +".txt")
        
#Creates a form for the users incorrect answers.
def create_incorrect_answer_form(username):
    with open("data/incorrect_answers_" + username +".txt", "a+") as file:
        new_file = file.read().splitlines()
        return new_file
        
# If the user enters nothing in the input field, this returns a string.
def empty_user_form():
    empty = "A username is required to play."
    return empty
    
def skip_final_score(username, score):
    return write_file("data/leaderboard.txt", "a", "{0} {1}".format(username, score))
    
# returns the question number, and number of questions displayed on the conundrum.html  
def question_number(page_number):
    return "Question {0} of {1}".format(page_number + 1 , number_of_questions()+1)

# This records the username and their final score to the leaderboard file.
def final_score(username, score):
    score = write_file("data/leaderboard.txt", "a", username + "\n" + str(score) +"\n")
    return score
  
# Takes off negative points when the question is guessed incorrectly or the answer is skipped.
def negative_points_one(score):
    if score == 0:
         score = 0
    else:
         score = score -1
    return score
    
def negative_points_two(score):
    if score == 0:
         score = 0
    else:
         score = score - 2
    return score
    
# For the leaderboard when sorting the top ten score, this sorts the seecond index postion. Called in leader_results().
def sort_score(x):
    return x[1]

#This reads the score and username from the leaderboard.txt file. Sorts the pairs into a dictionary and then sorts them by score order from highest to lowest.
def leader_results():
    lines = read_file("data/leaderboard.txt")
    name = []
    score = []
    for i, text in enumerate(lines):
        if i%2 ==0:
            name.append(text)
        else:
            score.append(text)
    name_and_score = zip(name,score)
      
    result = sorted(name_and_score, key = sort_score, reverse=True)
    print(result)
    return result

# This clears the incorrect answers from the users file.
def clear_Incorrect_answers(username):
    write_file("data/incorrect_answers_" + username +".txt", "w", "")

# Index Page--------------------------------------------------------------------
@app.route('/', methods=["GET", "POST"])
def index():
    page_number = 0
    score = 0
    
    
    if request.method == "POST":
        if request.form["username"] == "":    #If the username field is empty return a string.
            return render_template("index.html", empty = empty_user_form())
        
        else:
            create_incorrect_answer_form(request.form["username"])   #creates a new file for for the user in their name.
            clear_Incorrect_answers(request.form["username"])        #Clears any answers before entering. In case a user with the same name already created a file.
            return redirect(url_for('conundrum', username = request.form['username'], page_number = page_number, score = score ))
        
    return render_template("index.html")

# Questions and answers page----------------------------------------------------

@app.route('/conundrum/<username>/<int:page_number>/<int:score>', methods=["GET", "POST"])    

def conundrum(username, page_number, score):
    #This opens up a user named file for the users incorrect answers. created so other user incorrect answers don't add to another user. 
    
    userfile = "data/incorrect_answers_" + username +".txt"   # goes with os.remove(userfile) to delete the user file when the leaderboard is reached.
    if request.method == "POST":
        
        if page_number == number_of_questions():         # If the page number is equal to the total amount of questions
            answers = read_file("data/answers.txt")      # read from the answers
            
            for answer in (answers):
                
                if request.form["answer"] == answers[0 + page_number] and not 'skip' in request.form: # If the answer entered into the answer input box is the same as the index of answers.txt 
                    score = score + 10   # Add 10 points to the score
                    os.remove(userfile)  # remove the user incorrect answers file
                    final_score(username, score)    #This writes the final to the leaderboard.txt file 
                    return redirect(url_for('leaderboard', username = username, score = score))
                    
                elif 'skip' in request.form or number_of_incorrect_answers(username) == 9:   #If the skip botton is pressed or the user has had 9 incorrect answers, redirect to leaderboard.html .
                    #If the score is already at 0 remain at 0 and dont gain negative points, otherwise 2 points are deducted.
                    os.remove(userfile) 
                    final_score(username, score)
                    return redirect(url_for('leaderboard', username = username, score = negative_points_two(score)))
                    
                elif request.form["answer"] == "": #if the input field is empty, redirect to the same page
                    return redirect(url_for('conundrum', username = username, page_number = page_number, score = score))
                    
                elif request.form["answer"] != answers[0 + page_number]: # If the guess is not equal to the answers. 1 point is deducted from the score unless the score is already 0 
                    
                    write_incorrect_answer(username)  #Writes the incorrect answers to the users incorrect answer file.
                    return redirect(url_for('conundrum', username = username, page_number = page_number, score = negative_points_one(score)))
                
        
        elif page_number < number_of_questions(): # If the page number is less the total amount of questions
            
            answers = read_file("data/answers.txt")
                
            for answer in (answers):
                
                if request.form["answer"] == answers[0 + page_number] and not 'skip' in request.form:
                    clear_Incorrect_answers(username)
                    
                    return redirect(url_for('conundrum', username = username, page_number = page_number + 1, score = score + 10))
                    
                elif 'skip' in request.form or number_of_incorrect_answers(username) == 9:
                    negative_points_two(score)
                    return redirect(url_for('conundrum', username = username, page_number = page_number + 1, score = negative_points_two(score)))
                    
                elif request.form["answer"] == "":
                    return redirect(url_for('conundrum', username = username, page_number = page_number, score = score))
                    
                elif request.form["answer"] != answers[0 + page_number]:
                    write_incorrect_answer(username)
                    return redirect(url_for('conundrum', username = username, page_number = page_number, score = negative_points_one(score)))
   
    return render_template("conundrum.html", question = change_question(page_number), question_num = question_number(page_number), 
                                            page_number = page_number, username = username, score = score, incorrect = read_incorrect_answers(username), 
                                            userfile = userfile, guesses_remaining = remaining_guesses(username))
    
# Leaderboard ------------------------------------------------------------------
@app.route('/conundrum/leaderboard/<username>/<int:score>')
def leaderboard(username, score):
    
    results = leader_results() #prints out the leaderboard scores and usernames
    
    
    return render_template("leaderboard.html", results = results, username = username, score = score, total_points = (number_of_questions() + 1) * 10)
if __name__ == '__main__':
    app.run(host=os.getenv('IP'),port=int(os.getenv('PORT')),debug=True)
