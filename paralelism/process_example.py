from multiprocessing import Process

def countries(continent="Afica"):
    print(continent)
    return "finished printing"

if __name__ == "__main__":
    names = ["Ke","Tz","Ug","Sa","Ng","Za"]
    procs = []
    proc = Process(target=countries)
    procs.append(proc)
    proc.start()

    for name in names:
        proc = Process(target=countries,args=(name,))
        procs.append(proc)
        proc.start()