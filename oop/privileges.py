from random import choice
from user import User
  
class Privileges(User):
    def __init__(self, first_name: str, last_name: str, age: int, location: str):
        super().__init__(first_name, last_name, age, location)
        self.privileges = ["can add user","can ban user","can delete user"]

    def show_privileges(self):
        _ = choice(self.privileges)
        return f"The privileges are {_}"


a = Privileges(first_name="chris",last_name="sanit",age=23,location="nairobi")
print(a.describe_user())