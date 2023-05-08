from functools import wraps
import functools

def congrats(fn):
    print(type(fn))
    @functools.wraps(fn)
    def inner(*args,**kwargs):
        print("congratulations")
        return fn(*args,**kwargs)
    return inner
@congrats
def person(name):
    return f"{name}".capitalize()
print(person("saint"))
