import datetime

class Finance:

    def __init__(self,paid):
        self.__fees = 10_000
        self.paid = paid
        self.date = datetime.datetime.now()
    @property
    def balance(self):
        return self.__fees - self.paid

    def feesInfo(self):
        return f"Fees as per date of {self.date} is {self.__fees}"
    
    def justmethod(self):
        return "Hello I am just method"
    


class Student(Finance):
    school = "abc"

    def __init__(self, name, age, course, paid):
        self.name = name
        self.age = age
        self.course = course
        self._pin = "1234"
        self.date_created = datetime.datetime.now()        
        super().__init__(paid)
    
    def studentInfo(self):
        return f"The name {self.name} \t Age {self.age} \ncourse {self.course} \t date joined {self.date_created}"
    
    def getName(self):
        return self.name 

    def updateName(self,other):
        self.name = other
    
    def __eq__(self, other):
        True if self.age >= other else False

    @property
    def getPin(self):
        return self._pin
    
    
    def changePin(self,other):
        self._pin = other
        return f"{self.name} your pin has been change successfully"

    
    @staticmethod
    def getToday():
        return f"Todays date is {datetime.datetime.now()}"
        
    @classmethod
    def getSchool(cls):
        return cls.school
    
    def justmethod(self):
        return super().justmethod()
    
    
    

chris = Student("chris",23,"DEV",5000)
print(chris.balance)
print(chris.feesInfo())
print(chris.studentInfo())
print(Student.getSchool())
print(Student.getToday())
print(chris.getPin)
print(chris.changePin("hey"))
print(chris.getPin)
print(chris.justmethod())

    
    