import unittest
from run import app
import run
from flask import Flask, render_template, redirect, request, url_for, session
from flask_testing import TestCase

class test_app(unittest.TestCase):
    #test suite for conundrum
            
    def testing(self):
        """ 
        Test 1. Making sure the file is running
        """
        self.assertEqual(1, 1)
        
        
        
    def test_loading_questions(self):
        """ 
        Test 2. Testing that the questions have been loaded by checking there is a length.
        """
        file = run.read_questions()
        self.assertGreater(len(file), 0)
        
        
        
    def test_loading_answers(self):
        """ 
        Test 3. Testing that the answers have been loaded by checking there is a length.
        """
        file = run.read_answers()
        self.assertGreater(len(file), 0)
        
        
        
    def test_question_amount_equal_to_answer_amount(self):
        """ 
        Test 4. Making sure there are the same amount of questions as there are answers
        """
        question_length = run.read_questions()
        answer_length = run.read_answers()
        
        self.assertEqual(len(question_length), len(answer_length))
        
        
        
    def test_question_in_question_file(self):
        """ 
       Test 5. Testing that the correct questions are being read from the answers.txt file.
        """
        answer_file = run.read_questions()
        self.assertIn("What is always coming but never arrives?", answer_file)
        self.assertIn("I am black when clean and white when dirty. What am I?", answer_file)
        self.assertIn("Sometimes I walk in front of you. Sometimes I walk behind you. It is only in the dark that I ever leave you. What am I?", answer_file)
        self.assertIn("What comes down but never goes up?", answer_file)
        self.assertIn("What has a bed but doesn't sleep and a mouth but never eats?", answer_file)
        self.assertIn("I'm always hungry and must be fed, the finger I touch will soon turn red, what am I?", answer_file)
        self.assertIn("I can't be seen but I'm not a ghost. I can crack but I don't break. I can clap but I don't have any hands. I happen after a flash but I'm not a photo. I'm loud but I'm not music. What am I?", answer_file)
        self.assertIn("Who makes it, has no need of it. Who buys it, has no use for it. Who uses it doesn't know it. What is it?", answer_file)
        self.assertIn("I have seas without water, coasts without sand, towns without people and mountains without land. What am I?", answer_file)
        self.assertIn("I don't have eyes, but once I did see. Once I had thoughts, but now I'm white and empty. What am I?", answer_file)
        
        self.assertNotIn("This is not in", answer_file )
        
        
        
    def test_answer_in_answer_file(self):
        """ 
       Test 6. Testing that the correct answers are being read from the answers.txt file.
        """
        answer_file = run.read_answers()
        self.assertIn("tomorrow", answer_file)
        self.assertIn("chalkboard", answer_file)
        self.assertIn("shadow", answer_file)
        self.assertIn("rain", answer_file)
        self.assertIn("river", answer_file)
        self.assertIn("fire", answer_file)
        self.assertIn("thunder", answer_file)
        self.assertIn("coffin", answer_file)
        self.assertIn("map", answer_file)
        self.assertIn("skull", answer_file)
        self.assertNotIn("This is not in", answer_file )
        
        def test_get_index_page(self):
            response = app.test_client(self).get('/', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertIn('Welcome to Conundrum', str(response.data))
            
    
    def test_log_user_into_conundrum_page(self):
        """ 
       Test 7. Test to log a user in and prove they have reached the first question page.
        """
        with app.test_client(self) as client:
            with client.session_transaction() as session:
                session['score'] = 0
                session['page_number'] = 0
                session['message_display_number'] = 0
                session['display_points'] = 0
                session['last_incorrect_answer'] = ""
                
        data=dict(
            username= "user")
            
        response1 = client.post('/', content_type='multipart/form-data', data=data)
        self.assertEqual(response1.status_code, 302)
        self.assertIn('/conundrum/user', response1.location)
        
        response2 = client.get('/conundrum/user', content_type='html/text')
        self.assertEqual(response2.status_code, 200)
        self.assertIn('Welcome to Conundrum user', str(response2.data))
    
            
    def test_post_correct_answer_and_receive_10_points(self):
        """ 
       Test 8. Test that a correct answer on the first question page will redirect to the second question page and 
       a score has been received.
        """
        data=dict(
            answer= "tomorrow")
        
        with app.test_client(self) as client:
            with client.session_transaction() as session:
                session['score'] = 0
                session['page_number'] = 0
                session['message_display_number'] = 0
                session['display_points'] = 0
                session['last_incorrect_answer'] = ""
                
            response1 = client.get('/conundrum/user', content_type='html/text')    
            self.assertEqual(response1.status_code, 200)
            self.assertIn('Question 1 of 10', str(response1.data))
            self.assertIn('0 points', str(response1.data))

            response2 = client.post('/conundrum/user', content_type='multipart/form-data', data=data) 
            self.assertEqual(response2.status_code, 302)
            
            response3 = client.get('/conundrum/user', content_type='html/text')    
            self.assertEqual(response3.status_code, 200)
            self.assertIn('Question 2 of 10', str(response3.data))
            self.assertNotIn('Question 1 of 10', str(response3.data))
            self.assertIn('10 points', str(response3.data))
          
    def test_post_incorrect_answer_and_have_one_less_attempt(self):
        """ 
       Test 9. Test that a incorrect answer will redirect to the same page with one less attempt.
        """
        data=dict(
            answer= "today")
        
        with app.test_client(self) as client:
            with client.session_transaction() as session:
                session['score'] = 0
                session['page_number'] = 0
                session['message_display_number'] = 0
                session['display_points'] = 0
                session['last_incorrect_answer'] = ""
                
            response1 = client.get('/conundrum/user', content_type='html/text')    
            self.assertEqual(response1.status_code, 200)
            self.assertIn('Attempts Left:</b> 5', str(response1.data))
            self.assertIn('0 points', str(response1.data))

            response2 = client.post('/conundrum/user', content_type='multipart/form-data', data=data) 
            self.assertEqual(response2.status_code, 302)
            
            response3 = client.get('/conundrum/user', content_type='html/text')    
            self.assertEqual(response3.status_code, 200)
            self.assertIn('Attempts Left:</b> 4', str(response3.data))
            self.assertNotIn('Attempts Left:</b> 5', str(response3.data))
            self.assertIn('0 points', str(response3.data))
            
            
    
    def test_user_score_on_the_leaderboard(self):
        """ 
       Test 10. Test that the users score reaches the leaderbored. This test should be a result of 90 out of 100 
       however, this test recognises the incorrect answer from the last test
        """
        data=dict(
            answer= "Skull")
        
        with app.test_client(self) as client:
            with client.session_transaction() as session:
                session['score'] = 80
                session['page_number'] = 9
                session['message_display_number'] = 0
                session['display_points'] = 0
                session['last_incorrect_answer'] = ""
                
            response1 = client.get('/conundrum/user', content_type='html/text')    
            self.assertEqual(response1.status_code, 200)
            self.assertIn("Question 10 of 10", str(response1.data))
            self.assertIn('80 points', str(response1.data))
            
            response2 = client.post('/conundrum/user', content_type='multipart/form-data', data=data) 
            self.assertEqual(response2.status_code, 302)
            self.assertIn('/conundrum/leaderboard/user', response2.location)
            
            response3 = client.get('/conundrum/leaderboard/user', content_type='html/text')
            self.assertEqual(response3.status_code, 200)
            self.assertIn("your score is:  88 out of 100", str(response3.data))
        
    
    
            
            
"""
Test to score the different outcomes of answering the question correctly, skipping the question or guessing incorrectly.
When the answer is correct the page_number will increase by one and that will change the answer for the next question.
"""


def scoring(index, answer):
    page_number = 0 
    answer_file = run.read_answers()
    
    if index < 4:
        if answer == "skip":
            page_number +=1
            return -2
        elif answer == answer_file[index]:
            page_number +=1
            return 10
        else:
            return -1
    
    elif index == 9:
        if answer == "skip":
            return "redirected to the next page"
        elif answer == answer_file[index]:
            return "redirected to the next page"
        else:
            return -1
    
    
assert scoring(0, "tomorrow") == 10, "Answer doesn't match the question answer"
assert scoring(1, "chalkboard") == 10, "Answer doesn't match the question answer"
assert scoring(2, "shadow") == 10, "Answer doesn't match the question answer"
assert scoring(0, "fire") == -1, "Answer does match the question answer"
assert scoring(1, "river") == -1, "Answer does match the question answer"
assert scoring(2, "thunder") == -1, "Answer does match the question answer"

assert scoring(0, "skip") == -2, "answer is not skip"

assert scoring(9, "skull") == "redirected to the next page", "answer is not the last answer"
assert scoring(9, "skip") == "redirected to the next page", "answer is not the last answer"
assert scoring(9, "clouds") == -1, "answer is not the last answer"
