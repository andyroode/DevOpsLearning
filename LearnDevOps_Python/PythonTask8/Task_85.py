def letter_index(l):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    while i<len(alphabet):
        if l.lower()==alphabet[i].lower():
            index = i
            return index
        i = i + 1
    return -1


def new_index(word,index):
    alphabet = "abcdefghijklmnopqrstuvwxyz" #исходный алфавит
    i = 0 #начальное значение итератора
    new_index_str = "" #пустая строка для печати нового индекса
    new_word = "" #пустая строка с результатом
    while i<len(word):
        current_index = 0 #выставляем значение индекса буквы слова в оригинальном алфавите
        new_index = 0 #значение нового индекса выставляем нулевым
        if letter_index(word[i])>0:
            current_index = current_index + letter_index(word[i]) #присуждаем значение текущего индекса
            new_index = current_index + index #делаем обсчет нового индекса

            if abs(new_index) > len(alphabet)-1:
                if new_index < 0:
                    new_index = (len(alphabet)-1)-(abs(new_index)%len(alphabet))
                else:
                    new_index = new_index%len(alphabet)

            if new_index<0:
                new_index = (len(alphabet)-1)-((-1)*(new_index))

            new_index_str = new_index_str + str(new_index) + " "
            new_word = new_word + str(alphabet[new_index])

        else:
            print("Wrong wording, maybe it contains Numbers")
            return

        i = i + 1
    print("New indexes are:",new_index_str)
    print("New word is",new_word)






word = str(input("Please enter the original word >> "))
index = int(input("Please enter the code step >> "))
new_index(word,index)




