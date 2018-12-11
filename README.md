# Conundrum

- This is the third milestone project for the Full-Stack software development course through Code Institute. I named my project Conundrum as that's exactly what the user will have to go through.
The requirement for this project was to create a quiz game that would ask questions to the user. If the answer to the question is correct then the user would be directed to 
the next question. If the answer to the question is incorrect, then that incorrect answer would be displayed for the user to see. The user then would be able to have another shot at guessing 
the answer. After all the questions are answered, the user is directed to a leaderboard page with all the top scores.

- Heroku app 
  - https://conundrum.herokuapp.com/
- GitHub Repository 
  - https://github.com/brettcutt/conundrum

## Table of Contents

1. [UX](https://github.com/brettcutt/conundrum/blob/master/README.md#ux)
   - [Strategy](https://github.com/brettcutt/conundrum/blob/master/README.md#strategy)
   - [Features](https://github.com/brettcutt/conundrum/blob/master/README.md#features)
       - [Header and Footer](https://github.com/brettcutt/conundrum/blob/master/README.md#header-and-footer)
       - [index](https://github.com/brettcutt/conundrum/blob/master/README.md#index)
       - [Question page](https://github.com/brettcutt/conundrum/blob/master/README.md#question-page)
       - [leaderboard page](https://github.com/brettcutt/conundrum/blob/master/README.md#leaderboard-page)
    - [Wire Frames](https://github.com/brettcutt/conundrum/blob/master/README.md#wire-frames)
2. [Technologies, Libraries and Languages](https://github.com/brettcutt/conundrum/blob/master/README.md#technologies-libraries-and-languages)
3. [Testing](https://github.com/brettcutt/conundrum/blob/master/README.md#testing)
   - [Automated Tests](https://github.com/brettcutt/conundrum/blob/master/README.md#automated-testing)
   - [Manual Testing](https://github.com/brettcutt/conundrum/blob/master/README.md#manual-testing)
   - [Validation](https://github.com/brettcutt/conundrum/blob/master/README.md#code-validation)
4. [Deployment](https://github.com/brettcutt/conundrum/blob/master/README.md#deployment)
5. [Running the code locally](https://github.com/brettcutt/conundrum/blob/master/README.md#running-the-code-locally)
6. [Credits](https://github.com/brettcutt/conundrum/blob/master/README.md#credits)

## UX

### Strategy
- Design an app for those interested in solving logic based riddles. 
- As a user I would expect to be asked a question. If I answered correctly, I would receive some form of points and move onto the next 
question. If I answer incorrectly, I would expect to see no points and be able to try and guess the answer again. If I couldn't guess the answer I'd 
expect to be able to skip to the next question. To see how my score compares to everyone else, a leaderboard should show those results.

### Scope
#### features

##### Header and Footer
- A navigation bar with two links. One that redirects to the index page and the other that redirects to the leaderboard.
- A page icon that redirects to the index page.
- A GitHub icon that opens a new page to my GitHub repository.

##### index
- A login page where a visitor can create a username in the input field.

##### Question page.
- A welcome message is displayed greeting the user by their name.
- There is a section where the questions are displayed. 
- The user has a input field to enter their answer or a button to skip to the next question.
- When the user answers incorrectly, their answer will be displayed in the incorrect guesses section.
- There is a bar that displays the users current score, remaining amount of guesses and a button that when clicked, displays the games rules and
scoring.
- If the users remaining guesses reaches 0 than the question will be skipped to the next question.

##### leaderboard page
- Once the user has been through all of the questions, the page gets redirected to the leaderboard.
- This will show the users final score and a different message will display if they got on the leaderboard or not.
- A table shows the top ten scores and the name of the user that obtained that score.

### Wire Frames
- [Wire Frames](https://github.com/brettcutt/conundrum/blob/master/static/images/wireframes/wireframe.md)

## Technologies, Libraries and Languages

##### Python
Was used to: 
- Implement the logic, functionality and responses of the project.
- https://www.python.org/

##### Jquery
Was used to:
- Hide the welcome message in conundrum.html.
- Toggle to show and hide the game rules in conundrum.html.
- https://jquery.com/

##### BootStrap
Was used to:
- Make the app responsive on all devices e.g. using "col-xs-12".
- http://getbootstrap.com/

##### Flask
- A micro web framework written in Python.
- http://flask.pocoo.org/

##### HTML 5
Was used to:
- position and format the html elements.

##### CSS 3
Was used to:
- Style the HTML elements. 

##### Font Awesome
Was used for:
- the GitHub icon on the footer. 
- https://fontawesome.com/icons/github?style=brands
- https://fontawesome.com/license

##### Google Font
Was used for:
- For the font styles "rubik" and nanum gothic
- https://fonts.google.com/

### Testing 

#### Automated Testing
The automated test involves:
- If the project is ran locally, to run the tests enter `python test.py` and `python -m unittest`
- Click [here](https://github.com/brettcutt/conundrum/blob/master/test.py) to see my automated tests 

#### Manual Testing
To see the manual test file click [here](https://github.com/brettcutt/conundrum/blob/master/manual-testing.md).

### Code validation
**CSS**
- Using the jigsaw validator, the main.css file passed with no errors.

**HTML 5**
- Using W3C validator, the files returned no html5 related errors. Flask related errors were returned which is expected. 

**Python**
- There are no errors.

## Deployment
**In heroku**
- Created a new app called `conundrum`

- **In the terminal command line entered:**
  - `heroku login` Entered username and password.   
  - `git init` to Intilised a git repository.
  - `git remote add heroku https://conundrum.herokuapp.com/` to link the GitHub repository to the Heroku app.
  - `pip3 freeze --local > requirements.txt` Creates a .txt file which tells Heroku what dependencies the project is using.
  - `echo web: python run.py >procfile` Tells Heroku that this project is a web app and that "run.py" is going the run it.
  - `ps:scale web=1`
  - `git add`
  - `git commit -m "message"`
  - `git push -u heroku master`

- **In heroku**
  - Go to the project > setting > config vars
    - `IP | 0.0.0.0`
    - `PORT |  8080`
    - `SECRET_KEY | <your secret key>`
   - More > restart all dynos

- **The project can be found at:** https://conundrum.herokuapp.com/

## Running the code locally

- **In the terminal command line enter:**
  - `git clone https://github.com/brettcutt/conundrum.git`
  - `sudo pip3 install flask`

- **Create a env.py file:**
  - Inside type:
    - `import os`
    - `os.environ.setdefault('SECRET_KEY', '< your secrect key >')`

- **In the terminal command line enter:**
  - `python3 run.py`


## Credits
#### Content
- **The riddles cames from the following:**
  - https://www.braingle.com/brainteasers/104/who-makes-it-has-no-need-of-it.html
  - https://www.thesun.co.uk/fabulous/6885182/14-riddles-how-many-can-you-solve/
  - https://riddles.fyi/page/5/

#### Code
- **random secret key, understanding sessions**
  - https://www.youtube.com/watch?v=T1ZVyY1LWOg
  - https://stackoverflow.com/questions/42671298/python-counter-add-and-subtract
  - https://www.youtube.com/watch?v=T1ZVyY1LWOg

- **Sorting the leaderboard**
  - http://www.compciv.org/guides/python/fundamentals/sorting-collections-with-sorted/

- **Making the welcome message and scores disappear**
   - https://stackoverflow.com/questions/1911290/make-div-text-disappear-after-5-seconds-using-jquery

#### Media
- **background**
  - https://pixabay.com/en/earth-labyrinth-center-way-out-2293192/

- **Maze Icon**
  - I changed the color. Before it was in greyscale
  - https://pixabay.com/en/maze-icon-symbol-27465/

- **Font Awesome GitHub Icon**
  - https://fontawesome.com/icons/github?style=brands
  - https://fontawesome.com/license

#### Acknowledgements
- **My mentor Mossa Hassan**
  - Showing me more ways of debugging and watching responses.
  - Recommending sites to research
  - httpstatuses.com

- **The Code Institute slack forum**
  - Reading about other student questions, answers and problems greatly helps.
  - Good constructive criticism about the scoring from students Jo Wings and Eventyret.