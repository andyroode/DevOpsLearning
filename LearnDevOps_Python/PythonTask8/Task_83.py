def is_palindrome_new(word):
    max_index = len(word)
    if word[0:max_index:1]==word[::-1]:
        print("The word is palindrome!")

    else:
        print("The word is not palindrome!")
