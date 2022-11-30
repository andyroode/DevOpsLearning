
def has_no_e_initial():
    fin = open('../Book_example_tasks/words.txt')
    for i in fin:
        word = i.strip()
        e_flag = 'e' in word
        print(word,e_flag)

def has_no_e_counts():
    fin = open('../Book_example_tasks/words.txt')
    e_counter = 0
    all_words_counter = 0
    result_value = 0
    for i in fin:
        word = i.strip()
        if 'e' in word:
            e_counter = e_counter + 1
        else:
            print(word)
        all_words_counter = all_words_counter + 1
    result_value = (all_words_counter - e_counter)/all_words_counter
    result_value = result_value*100
    print("\n",result_value)


has_no_e_counts()