
def ceaser_decrypt(text:str, s:int) ->str:
    """
    Return string

    Takes a text and shift value and change postion
    """
    results = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            results += chr(ord(char) - s)
        elif char.isdigit():
            results += chr(ord(char) - s)
        elif char.isalpha():
            results += chr(ord(char) - s)
        else:
            results += chr(ord(char) - s)
    return results

if __name__=="__main__":
    text = str(input("type your text here: "))
    s=int(input("type shift: "))
    print(ceaser_decrypt(text,s))
    print("message:" +text, "shift: "+str(s))

