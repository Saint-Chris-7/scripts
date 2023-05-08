
def reverse(text) ->str:
    """
    Returns Str
    Takes a string and reverse the order
    """
    return "".join(reversed(text))

if __name__== "__main__":
    message = str(input("Please type your message here: "))
    print(reverse(message))


    