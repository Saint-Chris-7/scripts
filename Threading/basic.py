from random import random
from threading import Thread
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hello")
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hi")

t1 = Hi()
t2 = Hello()
t1.start()
t2.start()
t1.join()
t2.join()
print("helo world I am here today")