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
        self.assertIn("1. What is the capital of Australia?", answer_file)
        self.assertIn("2. What is the capital of Ireland?", answer_file)
        self.assertIn("3. What is the capital of England?", answer_file)
        self.assertIn("4. What is the capital of France?", answer_file)
        self.assertIn("5. What is the capital of Japan?", answer_file)
        self.assertNotIn("This is not in", answer_file )
        print("test_question_in_question_file \n")
        
        
        
    def test_answer_in_answer_file(self):
        """ 
       Test 5. Testing that the correct answers are being read from the answers.txt file.
        """
        answer_file = run.read_answers()
        self.assertIn("answer 1", answer_file)
        self.assertIn("answer 2", answer_file)
        self.assertIn("answer 3", answer_file)
        self.assertIn("answer 4", answer_file)
        self.assertIn("answer 5", answer_file)
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
    
    elif index == 4:
        if answer == "skip":
            return "redirected to the next page"
        elif answer == answer_file[index]:
            return "redirected to the next page"
        else:
            return -1
        print(page_number) 
    
    
assert scoring(0, "answer 1") == 10, "Answer doesn't match the question answer"
assert scoring(1, "answer 2") == 10, "Answer doesn't match the question answer"
assert scoring(2, "answer 3") == 10, "Answer doesn't match the question answer"
assert scoring(0, "answer 4") == -1, "Answer does match the question answer"
assert scoring(1, "answer 5") == -1, "Answer does match the question answer"
assert scoring(2, "answer 6") == -1, "Answer does match the question answer"

assert scoring(0, "skip") == -2, "answer is not skip"

assert scoring(4, "answer 5") == "redirected to the next page", "answer is not the last answer"
assert scoring(4, "skip") == "redirected to the next page", "answer is not the last answer"
assert scoring(4, "answer 1") == -1, "answer is not the last answer"

print("scoring passed")