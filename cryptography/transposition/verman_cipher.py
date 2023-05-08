#This is one-time pad subset of verman cipher
def encrypt(text,ciph) ->str:
    """
    Returns a string 
    
    Takes text and cipher string and change unicode of return value
    """

    assert len(text) == len(ciph), "The length of cipher and message are not equal"
    
    result = ""
    for i,j in zip(text,ciph):
        _ = ord(i) + ord(j)
        result += chr(_)
    return result
if __name__ == "__main__":
    print("The length of cipher == message and text only")
    message = str(input("Type your message: "))
    cipher =  str(input("Type your cipher text: "))
    print(encrypt(message,cipher))
    



        





