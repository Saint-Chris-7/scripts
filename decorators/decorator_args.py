import functools

def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

def say_wee():
    print("say, Whee!")

say_wee = do_twice(say_wee)
say_wee()

#returning values from a decorated fn
def do_twice_(func):
    functools.wraps(func)
    def wrapper_(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs) #this will return the return values of the decorated fn
    return wrapper_

@do_twice_
def hi(name):
    print("creating greeting")
    return f"hello,{name}"

print(hi("chris"))
print(hi)


