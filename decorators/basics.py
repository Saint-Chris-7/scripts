#this are the basics to understanding decorators

#1 higher order fucntions, fn taking another fn as args
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):#higher order fn
    return greeter_func("Bob")

print(greet_bob(be_awesome))
print(greet_bob(say_hello))


#2. a nested fn
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

#3. fn returning a fn
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num in range(0,10):
        return first_child() #ref to the fn
    elif num in range(10,20):
        return second_child() #ref to the fn

print(parent(11))
