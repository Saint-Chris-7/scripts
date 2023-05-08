def add(x:int,y:int) ->int:
    sum = x + y
    return sum
if __name__ == "__main__":
    x = int(input("number 1: "))
    y = int(input("number : "))
    z = add(x,y)
    print(z)
