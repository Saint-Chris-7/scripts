from unittest import TestCase
import unittest
from testing.class_survey import AnnonymousSurvey

class Test_Survey(TestCase):
    """test for class annonymous"""
    '''
    #test whether the response is stored in a list
    def test_store_single_response(self):
        myserv=AnnonymousSurvey("which language did you speak first? ")##create an object
        myserv.store_responses("English")#this is a response
        self.assertIn("English",container=myserv.responses,msg="to test response presence")
    def test_three_responses(self):
        myserv=AnnonymousSurvey("which language did you first learn")
        responses=['english','swahili','french']
        for response in responses:
            myserv.store_responses(response)
        for response in responses:
            self.assertIn(response,myserv.responses)
    '''

    """
    create a survey and response that will be used in all the test
    """
    def setUp(self):
        self.my_serv = AnnonymousSurvey("which language did you learn first ?")
        self.response=(['English','swahili','french'])

    def  test_single_response(self):
        self.my_serv.store_responses(self.response[0])
        self.assertIn(self.response[0],self.my_serv.responses)

    def test_three_response(self):
        for response in self.response:
            self.my_serv.store_responses(response)
        for response in self.response:
            self.assertIn(response,self.my_serv.responses)
        
        
    
    

if __name__=="__main__":
    unittest.main()

"""
this test is a it repetitive therefore we are going to user another feature of unittest tools
settup()
"""