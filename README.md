# Conundrum


- This is the third milestone project for the Full-Stack software development course through Code Institute. I named my project Conundrum as thats exactly what the user will have to solve.
The requirement of this project was to create a quiz game, that would ask the user questions for them to answer. If the answer to the question is correct then the user would be directed to 
the next question. If the answer to the question is incorrect, then that incorrect answer would be displayed for the user to see. The user than would be able to have another shot at guessing 
the answer. After all the questions are answered the user is directed to a leaderboard page with all the top scores.

- Heroku app https://conundrum.herokuapp.com/
- GitHub Repository https://github.com/brettcutt/conundrum

## UX

### Strategy
- Design an app for those interested in solving logic based riddles. 
- As a user I would expect to be asked a question. If I answer correctly I would receive some form of points and move onto the next 
question. If I answer incorrectly, I would expect to see negative points and be able to try and guess the answer again. If I couldn't guess the answer I'd 
expect to be able to skip to the next question.

### Scope
#### features

##### Head and Footer
- A navigation bar with two links. One that redirects to the index page and the other that redirects to the leaderboard.
- A page icon that redirects to the index page
- A GitHub icon that opens a new page to my GitHub repository.

##### index
- A login page where a visitor can create a username in the input field.

##### Question page.
- A welcome message is displayed greeting the user by their name. The box fades away when the "close" button is pressed
- There is a section where the questions are displayed. The user has a input field to enter their answer to the question or button to skip to the next question.
- When the user answers incorrectly, their answer will be displayed in the section next to the question.
- There is a bar that displays the users current score, remaining amount of guesses and a button that when clicked, displays the games rules and
scoring.
- If the users remaining guesses reaches 0 than the question be skipped to the next question.

##### leaderboard page
- Once the user has been through all of the questions, the page gets redirected to the leaderboard.
- This show the users final score and a different message will display if they got on the leaderboard or not.
- A table shows the top ten scores and the name of the user that obtained that score.
- If the user tries to go back, the page is redirected to the index page.

### Wire Frames
- [Wire Frames](https://github.com/brettcutt/conundrum/blob/master/static/images/wireframes/wireframe.MD)
## Technologies, Libraries and Languages

##### Python
Was used to: 
- Implement the logic, functionality and responses of the game.
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
Was used to:
- Implement python into html 5.
- http://flask.pocoo.org/

##### HTML 5
Was used to:
- position and format the elements in the app.

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
- For the font style "rubik"
- https://fonts.google.com/

### Testing 

#### Automated Testing
The automated test involves: 
- Checking if a txt file has content with self.assertGreater(len(file), 0)
- Making sure that it contains the infomation that is suppose to be in a particular file with "assetIn" and checking infomation that isn't in the file with "assertNotIn".
- Check that there are the dame amount of answers as there are questions.
- Making sure that the score works, if the user correctly answers the question, they get +10 points. An Incorrect answer is -1 point and a skip is -2 points. If the user is on the last page, a correct answer
or skip returns a string saying they've been redirected. A incorrect answer again only deduct 1 point.
- Click [here](https://github.com/brettcutt/conundrum/blob/master/test.py) to see my automated tests 

#### Manual Testing

##### Index.html and base.html(header and footer)
The manual test involved checking: 
- The maze icon redirects back the the index (home) page.
- The "Home" navigation link redirects back to the index (home) page.
- The "Leaderboard" navigation link redirects to the leaderboard (leaderboard.html) page.
- The username input field when submitted with no text, rerenders the index.html page and returns a string saying to enter a user name.
- That entering a username and submitting redirects to the conundrum.html page.
- Clicking the GitHub icon opens a new page to my GitHub repository.

##### conundrum.html
The manual test involved checking:
- The users file for incorrect answers is created.
- The welcome message fades away when the close button is clicked.
- The rules button toggles rules box as well as the close button only hiding the box.
- Submitting an empty input field redirects to the same page and keeps any incorrect answers if there are any. 
- Entering a incorrect answer: deducts 1 point from the score, deduct 1 remaining guess and displays that answer in the "incorrect guesses" box.
- Correct and incorrect answers, and skips are displayed in the questions container including the amount added or taken off.
- Entering an incorrect answer 10 times redirects to the next page as well as having a total of 10 points deducted plus another point because it also a skip.
- Answering correctly redirects to the next question, adds 10 points to the score, clears the incorrect answers and refreshes the remaining guesses.
- All links work and redirect to the appropriate pages.
- The different combination of correct answers, incorrect answers, skips all total the score up appropriately.


##### leaderboard.html
The manual test involved checking:
- The users file for incorrect answers is deleted.
- If the users final score is the correct score, and if it is greater than the 10th position and message displays saying well done for making the leaderboard. If the score is less
than the 10th position a message displays saying sorry you didn't make the leaderboard.
- The leaderboard displays the top ten scores 
- If the user tries to go back to the last question, the page redirects to the index(home) page.
- The users file for incorrect answers is deleted.
- All links work and redirect to the appropriate pages.

#### Testing Issues
##### Reading file from Heroku 
- My incorrect answers were not being display on the conundrum.html page, which I found the problem came from how it was being read as
a "a+" file. I created another "r" type reading file to solve this. Cloud 9 runs python 2.6.7 by default and my project worked fine on that, but it wasn't until I pushed my project 
to heroku that I found problems when it was running python 3.

##### Multiple players
- I originally had a incorrect_answers.txt file. When multiple users were playing at the same time, incorrect answers that belonged to one user would appear for another. 
- To solve this, when the user inputs a username, a incorrect_answers_username.txt file is created. This works well for multiple users and their individual answers.

##### Going back
- Another frustration during this project was going back. If I answered incorrectly on one question and then decided to go back to a previous question, the incorrect answer would display in the 
incorrect answers section of that question. Sessions seemed to solve this issue. When the user tries to go back they will stay on the same question, and multiple back requests redirects to the index(home) page.
- When users get to the leaderboard, there was the option that they could go back to the last question. I wanted to make sure they couldn't go back and if the did try, they 
would be directed to the index page. 
- I used the "os.remove(userfile)" code to delete the users incorrect_answers_username.txt file once they reached the leaderboard screen. 
Then I searched for a code that checked if the users file exists. Then in an if statement, if the users file doesn't exist they will be redirected to the index page.
- https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists
- os.path.exists(userfile)

##### Keeping a count
- One of the more frustrating issues was keeping track of a score. Originally if the user answered the question correctly I expected a count to += 1. When the answer was submited ("POST") the count would increase to 1.
However when the page redirected ("GET") the count would reset back to 0. 
- My next idea was adding "1" to a count.txt file and reading the length when a question was answered correctly, but this became a problem when multiple users were playing. It would affect the scores and questions others 
-users had
where using the same points sheet.
- I had seen on another project that score(count) was recorder in the endpoint. I used this method for most of my project when building it. I wasn't 
really happy with this method because I could cheat by manually entering a score in the endpoint, which would end up on the leaderboard. 
- While searching through the slack forum other students were wrting about sessions and user sessions. I looked more into this and found that sessions would keep a count.
- https://stackoverflow.com/questions/42671298/python-counter-add-and-subtract
- https://www.youtube.com/watch?v=T1ZVyY1LWOg

## Deployment
#### In heroku
- Created a new app

#### In the terminal command line enter:
##### heroku login
- Entered username and password.

##### cd conundrum/
- Moved to the project directory.

##### git init
- Intilised a git repository.

##### git remote add heroku https://conundrum.herokuapp.com/
- Linked the GitHub repository to the Heroku app.

##### pip3 freeze --local > requirements.txt
- Tells Heroku what languages the project is using and creates a file with the dependencies.

##### echo web: python run.py >procfile
- Tells Heroku that this project is a web app and the "run.py" is going the run it. 

##### ps:scale web=1

##### git add
##### git commit -m "message"
##### git push -u heroku master
- pushes the project to Heroku.

#### In heroku
##### Go to the project > setting > config vars
- key = IP: value = 0.0.0.0
- key = PORT: value = 8080

##### More > restart all dynos

##### The project can be found at https://conundrum.herokuapp.com/

## Running the code locally
### In the terminal command line enter:
##### git clone https://github.com/brettcutt/conundrum.git
##### sudo pip3 install flask
- Installs Flask
 
##### Hit the run button on run.py

## Credits
### Content
Add where the riddles came from here

### Code
##### random secret key, understanding sessions
- https://www.youtube.com/watch?v=T1ZVyY1LWOg
- https://stackoverflow.com/questions/42671298/python-counter-add-and-subtract
- https://www.youtube.com/watch?v=T1ZVyY1LWOg

##### Sorting the leaderboard
http://www.compciv.org/guides/python/fundamentals/sorting-collections-with-sorted/

##### Making the welcome message and scores disappear
- https://stackoverflow.com/questions/1911290/make-div-text-disappear-after-5-seconds-using-jquery

### Media
##### background
- https://pixabay.com/en/earth-labyrinth-center-way-out-2293192/

##### Maze Icon
- I changed the color and before it was in greyscale
- https://pixabay.com/en/maze-icon-symbol-27465/

##### Font Awesome GitHub Icon
- https://fontawesome.com/icons/github?style=brands
- https://fontawesome.com/license

### Acknowledgements
##### My mentor Mossa Hassan
- Showing me more ways of debugging and watching responses.
- Recommending sites to research
- httpstatuses.com

##### The Code Institute slack forum
-Reading about other student questions, answers and problems greatly helps.  
 

things to fix:

single digits appearing on the leaderboard

