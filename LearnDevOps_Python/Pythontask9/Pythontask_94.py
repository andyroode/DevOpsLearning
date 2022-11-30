def uses_only(letters):
    fin = open("../Book_example_tasks/words.txt")

    for i in fin:
        control_flag = False
        word = i.strip()
        for j in letters:
            if j in word:
                control_flag = True

        if control_flag == True:
            print(word)

uses_only("zn")

