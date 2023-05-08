import random
class User:
    def __init__(self,first_name:str,last_name:str,age:int,location:str):
        self.age= age
        self.last_name = last_name
        self.first_name = first_name
        self.location = location
        self.login_attempt = 1

    def login_attempts(self,attempt:int):
        self.login_attempt = attempt
    
    def increment_login_attempts(self,attempts:int):
        self.login_attempt += attempts
    
    def reset_login_attempts(self):
        self.login_attempt = 1

    def describe_user(self):
        print(f"This is user profile: Fist name: {self.first_name} Last Name: {self.last_name} Age: {self.age} Location: {self.location}\
            login attempts: {self.login_attempt}")

    def greet_user(self):
        list_ = ["Good morning","Good afternoon","Hey there","hi","welcome","Guten mogen"]
        greets = random.choice(list_)
        print(f"{greets}, {self.first_name}")
if __name__== "__main__":
    chris = User(first_name="chris",last_name="Muriuki",age=21,location="JUja")
    chris.greet_user()
    chris.describe_user()