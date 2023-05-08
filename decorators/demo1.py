def ordinary(func):
    def wrapper():
        print("This function has been decorated!!")
        func()
        print("The decorated fn after being called")
    return wrapper

def pretty():
    print("I want to be decorated")

pretty = ordinary(pretty)
pretty()

print()
print()
print()

@ordinary
def i_want():
    print("A waiting decoration")
i_want()