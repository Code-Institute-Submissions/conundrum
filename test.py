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
        
        
        
    def test_1_loading_questions(self):
        """ 
        Test 2. Testing that the questions have been loaded by checking there is a length.
        """
        file = run.read_questions()
        self.assertGreater(len(file), 0)
        print("Test_load_questions passed!\n")
        
        
        
    def test_2_loading_answers(self):
        """ 
        Test 3. Testing that the answers have been loaded by checking there is a length.
        """
        file = run.read_answers()
        self.assertGreater(len(file), 0)
        print("Test_load_answers passed!\n")
        
        
        
    def test_3_question_amount_equal_to_answer_amount(self):
        """ 
        Test 4. Making sure there are the same amount of questions as there are answers
        """
        question_length = run.read_questions()
        answer_length = run.read_answers()
        
        self.assertEqual(len(question_length), len(answer_length))
        print("amount_of_answers_equal_to_questions passed!")
        print("question length = {0}. answer length = {1} \n".format(len(question_length), len(answer_length)))
        
        
        
    def test_4_question_in_question_file(self):
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
        print("test_question_in_question_file \n")
        
        
        
    def test_5_answer_in_answer_file(self):
        """ 
       Test 5. Testing that the correct answers are being read from the answers.txt file.
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

print("scoring passed")