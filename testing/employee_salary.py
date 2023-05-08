class Employee(object):
    def __init__(self, first:str,last:str,salary:int):
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, other=5000):
        return self.salary + other


a = Employee("chris","Gathuthi",2000)
print(Employee.give_raise(a))



        
        