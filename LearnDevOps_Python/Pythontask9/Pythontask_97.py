def check_Three():
    fin = open("../Book_example_tasks/words.txt")
    result_word=""
    for i in fin:
        word = i.strip()
        j=0
        counter=0
        while j<len(word)-1:
            if word[j]==word[j+1]:
                counter = counter+1
            j = j + 1
        if counter>=3:
            result_word = word
            h = 0
            checkFlag = False
            while (h < len(result_word)-1) and (h+5<=(len(result_word)-1)):
                if (result_word[h] == result_word[h+1]) and (result_word[h+2] == result_word[h+3]) and (result_word[h+4] == result_word[h+5]):
                    checkFlag = True
                    break
                h = h + 1
            if checkFlag == True:
                print(result_word)



check_Three()