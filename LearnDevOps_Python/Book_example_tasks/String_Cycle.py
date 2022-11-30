def find(word,letter,index):
    if (index>len(word)-1) or index<0:
        print("Start index of search is more than length of the word OR less than zero value!")
        return -1

    while index<=len(word)-1:
        if word[index] == letter:
            print("Index of letter",letter," is",index)
            return index
        index = index + 1
    return -1


word = str(input("Please enter the word >"))
letter = str(input("Please enter the letter > "))
index = int(input("Please enter the start index > "))

find(word,letter,index)