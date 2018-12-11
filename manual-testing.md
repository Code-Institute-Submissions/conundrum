## Manual Testing

## Table of Contents

- [Manual Tests](https://github.com/brettcutt/conundrum/blob/master/manual-testing.md#manual-tests)
  - [Homepage, header and footer](https://github.com/brettcutt/conundrum/blob/master/manual-testing.md#homepage-header-and-footer)
  - [Conundrum page](https://github.com/brettcutt/conundrum/blob/master/manual-testing.md#conundrum-page)
  - [Leaderboard page](https://github.com/brettcutt/conundrum/blob/master/manual-testing.md#leaderboard-page)
- [Checklist](https://github.com/brettcutt/conundrum/blob/master/manual-testing.md#checklist)
- [Responsiveness](https://github.com/brettcutt/conundrum/blob/master/manual-testing.md#responsiveness)
- [Multiple players](https://github.com/brettcutt/conundrum/blob/master/manual-testing.md#multiple-players)
- [Testing Issues](https://github.com/brettcutt/conundrum/blob/master/manual-testing.md#testing-issues)
   - [Reading file from Heroku](https://github.com/brettcutt/conundrum/blob/master/manual-testing.md#reading-file-from-heroku)
   - [Multiple players](https://github.com/brettcutt/conundrum/blob/master/manual-testing.md#multiple-players)
   - [Going back](https://github.com/brettcutt/conundrum/blob/master/manual-testing.md#going-back)
   - [Keeping a count](https://github.com/brettcutt/conundrum/blob/master/manual-testing.md#keeping-a-count)
   - [Student-testing](https://github.com/brettcutt/conundrum/blob/master/manual-testing.md#student-testing)
   - [UnicodeDecodeError](https://github.com/brettcutt/conundrum/blob/master/manual-testing.md#unicodedecodeerror)

### Manual tests
##### Homepage, header and footer)
- A
  - The maze icon redirects back the the index (home) page.
  - The "Home" navigation link redirects back to the index(home) page.
  - The "Leaderboard" navigation link redirects to the leaderboard(leaderboard.html) page.
  - The username input field when submitted with no text, rerenders the index.html page and returns a string saying to enter a user name.
  - That entering a username and submitting, redirects to the conundrum.html page.
  - Clicking the GitHub icon opens a new page to my GitHub repository.

##### Conundrum page
- B
  - The users file for incorrect answers is created.
  - The welcome message fades away after 2 seconds.
  - The "rules" button toggles the rules box as well as the "close" button only hides the box.
  - Submitting an empty input field redirects to the same page and keeps any incorrect answers if there are any. 
  - Entering a incorrect answer displays the incorrect answer on the redirected page.
  - Entering an incorrect answer 5 times redirects to the next question. The redirected page displays a message for 2 seconds saying " 'answer' is incorrect. question skipped, +0 points", incorrect answers are cleared.
  - Answering correctly redirects to the next question, adds (10 - (the number of incorrect guesses * 2)) to the score and displays a 2 second message saying "'answer' is correct +'num' points".
  - On the last question: answering correctly, skipping or answering incorrectly 5 times redirects to the leaderboard screen.
  - All links work and redirect to the appropriate pages.
  - The different combination of correct answers, incorrect answers, skips all total the score up appropriately.

##### Leaderboard page
- C
  - The users file for incorrect answers is deleted.
  - If the users final score is greater than the 10th position on the leaderboard, a message displays saying "well done for making the leaderboard". If the score is less
  than the 10th position, a message displays saying "sorry you didn't make the leaderboard".
  - The leaderboard displays the top ten scores 
  - If the user tries to go back to the last question, the page redirects to the index(home) page.
  - All links work and redirect to the appropriate pages.
  
#### Checklist

|Pass|Fail|
|:--:|:--:|
|P|F|

|     |Chrome|FireFox|Edge|Opera|Safari|Mobile|
|:---|:----:|:-----:|:--:|:---:|:----:|:----:|
|**A. i**|      P|P|P|P|P|P|
|**A. ii**|     P|P|P|P|P|P|
|**A. iii**|    P|P|P|P|P|P|
|**A. iv**|     P|P|P|P|P|P|
|**A. v**|      P|P|P|P|P|P|
|**A. vi**|     P|P|P|P|**F**|P|  
|**B. i**|      P|P|P|P|P|P|
|**B. ii**|     P|P|P|P|P|P|
|**B. iii**|    P|P|P|P|P|P|
|**B. iv**|     P|P|P|P|P|P|
|**B. v**|      P|P|P|P|P|P|
|**B. vi**|     P|P|P|P|P|P|
|**B. vii**|    P|P|P|P|P|P|
|**B. viii**|   P|P|P|P|P|P|
|**B. ix**|     P|P|P|P|P|P|
|**B. x**|      P|P|P|P|P|P|
|**C. i**|      P|P|P|P|P|P|
|**C. ii**|     P|P|P|P|P|P|
|**C. iii**|    P|P|P|P|P|P|
|**C. iv**|     P|P|P|P|P|P|
|**C. v**|      P|P|P|P|P|P|


###### note on FireFox
- Going backwards from the leaderboard page went back to the last question. However if the user tried to answer again, then the page redirected back to the index(home) page.
I don't find this a problem because the user still cannot cheat and change their score.

##### Note on Safari
- The GitHub icon couldn't secure a connection to the server.
- I'm running safari on windows. The last version update was back in 2012. This would suggest that this version of browser lacks some support.   


#### Responsiveness
- Using the developer tools in chrome and my own personal mobile phone, all the device selections were used to check the responsiveness of this project.
- Every part of the project is appropriately responsive.

#### Multiple players
- To ensure that the project ran with multiple player and didn't clash, I used my computer and a friends computer, logged in as different users and played the project at the same time. 
- There was no outcome where a player was affected by another.

#### Testing Issues
##### Reading file from Heroku 
- My incorrect answers were not being display on the conundrum.html page, which I found the problem came from how it was being read as
a "a+" file. I created another "r" type reading file to solve this. Cloud 9 runs python 2.6.7 by default and my project worked fine on that, but it wasn't until I pushed my project 
to heroku that I found problems when it was running python 3.

##### Multiple players
- I originally had a incorrect_answers.txt file. When multiple users were playing at the same time, incorrect answers that belonged to one user would appear for another. 
- To solve this, when the user inputs a username, a incorrect_answers_"username".txt file is created. This works well for multiple users and their individual answers.

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
- One of the more frustrating issues was keeping track of a score. Originally if the user answered the question correctly, I expected a count to += 1. When the answer was submited ("POST") the count would increase to 1.
However when the page redirected ("GET") the count would reset back to 0. 
- My next idea was adding "1" to a count.txt file and reading the length when a question was answered correctly, but this became a problem when multiple users were playing. It would affect the scores and questions other
users had when using the same points sheet.
- I had seen on another project that score(count) was recorder in the endpoint. I used this method for most of my project when building it. I wasn't 
really happy with this method because I could cheat by manually entering a score in the endpoint, which would end up on the leaderboard. 
- While searching through the slack forum, other students were wrting about sessions and user sessions. I looked more into this and found that sessions would keep a count.
- https://stackoverflow.com/questions/42671298/python-counter-add-and-subtract
- https://www.youtube.com/watch?v=T1ZVyY1LWOg

##### Student testing
- I allowed friends, family and other code institute students to test my project. The only constructive criticism I recieved was from fellow students about the style of scoring. Originally I had each correct answer 
being worth 10 points, incorrect answers were worth -1 point and a skip was worth -5 points. This scoring system allowed the user to achieved an overall negative score which didn't seen right by others.
Instead of losing points on skips and incorrect answers, the scoring changed so that if the answer was correctly guessed, the question would be worth 10 points and 2 points were deducted for each incorrect answer.
So if the user guessed incorrectly 5 times or skipped they would be redirected to the next question and lose no points.

##### UnicodeDecodeError
- After copying and pasting riddles in the quetions.txt file, I kept on receiving an error on the second question. This was due to a foreign apostrophe character,
which was difficult to identify but something small that was causing the error. 