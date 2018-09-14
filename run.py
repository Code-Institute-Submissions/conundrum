import os 
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect("conundrum/" + request.form["username"])
        
    return render_template("index.html")
@app.route('/conundrum/<username>', methods=["GET", "POST"])    

def conundrum(username):
    return render_template("conundrum.html")

app.run(host=os.getenv('IP'),port=int(os.getenv('PORT')),debug=True)