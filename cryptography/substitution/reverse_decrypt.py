
def reverse_decrypt(text) ->str:
    """
    Returns a string

    Takes a string and reverse order, reverse an already reversed string
    """

    return text[::-1]

if __name__=="__main__":
    text = str(input("type the text to decrypt: "))
    print(reverse_decrypt(text))
    