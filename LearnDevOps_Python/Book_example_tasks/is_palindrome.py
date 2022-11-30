def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]


def palindrome(word):
    checkVal=False #setting the default palindrome flag to False
    if len(word)>2: #Check the string length
        if first(word) == last(word): #Check the first and last letter
            checkVal = True #if a palindrome - flag to True
            mid = middle(word)
            if (len(mid)==2 and first(mid)==last(mid)) or (len(mid)==1):
                return True
            elif len(mid)>2:
                palindrome(mid)
        else:
            return False
    return checkVal


if palindrome("topot"):
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")






