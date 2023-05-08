from multiprocessing import Process
import os
import time
processes = []
num_processes = os.cpu_count()

def sq():
    for i in range(100):
        i*i
        time.sleep(0.1)
#create process
for i in range(num_processes):
    p = Process(target =sq)
    processes.append(p)

#start 
for p in processes:
    p.start()
#join 
for p in processes:
    p.join()
print("end main")