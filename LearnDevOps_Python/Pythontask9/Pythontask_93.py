def avoids(letters):
    fin = open("../Book_example_tasks/words.txt")
    for i in fin:
        not_in_list = False
        word = i.strip()
        for j in letters:
            if j not in word:
                not_in_list = True
            else:
                not_in_list = False
                break
        if not_in_list == True:
            print(word)

avoids("zn")



