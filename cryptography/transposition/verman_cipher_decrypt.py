#This is one-time pad subset of verman cipher
def decrypt(text:str,ciph:str) ->str:
    """
    Returns a string 
    
    Takes text and cipher string and change unicode of return value
    """
    assert len(text) == len(ciph), "The length of cipher and message are not equal"
    
    result = ""
    for i,j in zip(text,ciph):
        _ = ord(i) - ord(j)
        result += chr(_)
    return result
if __name__ == "__main__":
    print("The length of cipher == message")
    message = str(input("Type your encrypted message: "))
    cipher =  str(input("Type your cipher text: "))
    print(decrypt(message,cipher))
    



        





