
"""this is a class that collects annonymous survery form questions"""
class AnnonymousSurvey:
    def __init__(self, questions):
        """store the questions and prepare to store the responeses"""

        self.questions = questions
        self.responses =[]

    def show_questions(self):
        """show the survey questions"""
        print(f"{self.questions}")
    def store_responses(self,new_responses):
        """this stores new responses"""
        self.responses.append(new_responses)
    
    def show_results(self):
        """show all the results"""
        print(f"this is the survey")

        for resp in self.responses:
            if resp is None:
                print("no survey conducted")
            print(f"{resp}")

        