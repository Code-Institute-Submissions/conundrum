import unittest
import run

class test_run(unittest.TestCase):
    #test suite for conundrum
    
    def testing(self):
        """ 
        Test 1. Making sure the file is running
        """
        self.assertEqual(1, 1)
        print("Initial test passed! \n")
        
        
        
    def test_loading_questions(self):
        """ 
        Test 2. Testing that the questions have been loaded by checking there is a length.
        """
        file = run.read_questions()
        self.assertGreater(len(file), 0)
        print("Test_load_questions passed!\n")
        
        
        
    def test_loading_answers(self):
        """ 
        Test 3. Testing that the answers have been loaded by checking there is a length.
        """
        file = run.read_answers()
        self.assertGreater(len(file), 0)
        print(".Test_load_answers passed!\n")
        
        
        
    def test_question_amount_equal_to_answer_amount(self):
        """ 
        Test 4. Making sure there are the same amount of questions as there are answers
        """
        question_length = run.read_questions()
        answer_length = run.read_answers()
        
        self.assertEqual(len(question_length), len(answer_length))
        print("amount_of_answers_equal_to_questions passed!")
        print("question length = {0}. answer length = {1} \n".format(len(question_length), len(answer_length)))
        
        
        
    def test_question_in_question_file(self):
        """ 
       Test 5. Testing that the correct questions are being read from the answers.txt file.
        """
        answer_file = run.read_questions()
        self.assertIn("What flies without eyes and cries without eyes?", answer_file)
        self.assertIn("I'm always hungry and must be fed, the finger I touch will soon turn red, what am I?", answer_file)
        self.assertIn("What has a bed but doesn't sleep and a mouth but never eats?", answer_file)
        self.assertIn("I have a brother that you can see but not hear. When I come after my brother and you can hear me but not see me. What am I?", answer_file)
        self.assertIn("Who makes it, has no need of it. Who buys it, has no use for it. Who uses it doesn't know it. What is it?", answer_file)
        self.assertIn("I have seas without water, coasts without sand, towns without people and mountains without land. What am I?", answer_file)
        self.assertIn("I don't have eyes, but once I did see. Once I had thoughts, but now I'm white and empty. What am I?", answer_file)
        self.assertIn("I can be written, I can be spoken, I can be exposed, I can be broken. What am I?", answer_file)
        self.assertIn("This old one runs forever but never moves at all. It has no lungs but has a mighty roar. What am I?", answer_file)
        self.assertIn("I go up and I go down, towards the sky and the ground. I'm present and past tense too. What am I?", answer_file)
        
        self.assertNotIn("This is not in", answer_file )
        print("test_question_in_question_file \n")
        
        
        
    def test_answer_in_answer_file(self):
        """ 
       Test 5. Testing that the correct answers are being read from the answers.txt file.
        """
        answer_file = run.read_answers()
        self.assertIn("clouds", answer_file)
        self.assertIn("fire", answer_file)
        self.assertIn("river", answer_file)
        self.assertIn("thunder", answer_file)
        self.assertIn("coffin", answer_file)
        self.assertIn("map", answer_file)
        self.assertIn("skull", answer_file)
        self.assertIn("news", answer_file)
        self.assertIn("waterfall", answer_file)
        self.assertIn("seesaw", answer_file)
        self.assertNotIn("This is not in", answer_file )
        print("test_answer_in_answer_file passed \n")
            
            
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
        print(page_number)  
    
    elif index == 9:
        if answer == "skip":
            return "redirected to the next page"
        elif answer == answer_file[index]:
            return "redirected to the next page"
        else:
            return -1
        print(page_number) 
    
    
assert scoring(0, "clouds") == 10, "Answer doesn't match the question answer"
assert scoring(1, "fire") == 10, "Answer doesn't match the question answer"
assert scoring(2, "river") == 10, "Answer doesn't match the question answer"
assert scoring(0, "fire") == -1, "Answer does match the question answer"
assert scoring(1, "river") == -1, "Answer does match the question answer"
assert scoring(2, "thunder") == -1, "Answer does match the question answer"

assert scoring(0, "skip") == -2, "answer is not skip"

assert scoring(9, "seesaw") == "redirected to the next page", "answer is not the last answer"
assert scoring(9, "skip") == "redirected to the next page", "answer is not the last answer"
assert scoring(9, "clouds") == -1, "answer is not the last answer"

print("scoring passed")