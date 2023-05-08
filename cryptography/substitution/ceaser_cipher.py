#A python program to illustrate Caesar Cipher Technique

def encrypt(text,s):

    """
    Return string
    takes a string and int, shift text postion by the int
    """

    results = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            results += chr(ord(char) + s)
        elif char.isdigit():
            results += chr(ord(char) + s)
        elif char.isalpha():
            results += chr(ord(char) + s)
        else:
            results += chr(ord(char) + s)
    return results

if __name__ == "__main__":
    text = str(input("Type your text here: "))
    s = int(input("shift position: "))
    print(encrypt(text,s))
    print("message "+text, "shift "+str(s))
    print("Ecryption complete----- ok")



