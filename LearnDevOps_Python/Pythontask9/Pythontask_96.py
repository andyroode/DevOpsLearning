def is_abecedarian():
    fin = open("../Book_example_tasks/words.txt")
    for i in fin:
        word = i.strip()
        j = 0
        word_check_flag = False
        while j < len(word)-1:
            if word[j]<=word[j+1]:
                word_check_flag = True
            else:
                word_check_flag = False
                break
            j = j + 1

        if word_check_flag == True:
            print(word)



is_abecedarian()




