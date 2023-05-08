#this is an example of a deorator

def my_decorator(func):
    def wrapper():
        print("something is happening before the function is callled")
        func()
        print("something is happening after the fn is called")
    return wrapper

def say_wee():
    print("Say Whee!")

say_wee = my_decorator(say_wee)
say_wee()

