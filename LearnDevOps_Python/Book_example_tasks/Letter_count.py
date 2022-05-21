def letter_count(word, letter,start_index):
    if (start_index>len(word)-1) or start_index<0:
        print("Start index of search is more than length of the word OR less than zero value!")
        return -1

    count = 0
    while start_index<=len(word)-1:
        if word[start_index]==letter:
            count = count + 1
        start_index = start_index+1
    return count






word = str(input("Please enter the word > "))
letter = str(input("Please enter the letter > "))
start_index = int(input("Please enter the start index > "))
print("Letter",letter,"was found",letter_count(word,letter,start_index),"times.")

