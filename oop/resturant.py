
import random

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name= restaurant_name
        self.cuisine_type = cuisine_type
        self.number_serverd = 0
        
    
    def set_number_served(self,number:int):
        self.number_serverd = number

    def increment_number_served(self,number):
        self.number_serverd += number
    
    def describe_restaurant(self):
        print(f"The restaurant descriptions are Name: {self.restaurant_name}, Cuisine: {self.cuisine_type},\
            customer served {self.number_serverd}")

    def open_restaurant(self):
        print(f"The restaurant is open")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors =["vanilla","strawberry","choco","shake"]
    
    def show_flavors(self):
        print(f"Available flavours are; {self.flavors}")

if __name__=="__main__":
    seas= Restaurant("KFC","fried chicken")
    seas.describe_restaurant()

    pep = IceCreamStand("Peppinos","Pizza")
    pep.show_flavors()
    pep.describe_restaurant()








