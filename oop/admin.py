from privileges import Privileges

class Admin(Privileges):
    def __init__(self, first_name: str, last_name: str, age: int, location: str):
        super().__init__(first_name, last_name, age, location)
        
if __name__ == "__main__":
    chris = Admin(first_name="chris",last_name="Cath",age=20,location="Juja")
    chris.show_privileges()    

