fin = open('words.txt')
count = 0
for i in fin:
    word = i.strip()
    if len(word)>20:
        count = count + 1


