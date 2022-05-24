fin = open('../Book_example_tasks/words.txt')
count = 0
for i in fin:
    word = i.strip()
    if len(word)>20:
        count = count + 1

print(count)