#Программа которая выдает уникальные значения одометра. При увелечении на километр появляются новые полиндромы.
def show_possible_vals():
    j = 100000
    max_value = 999999
    while j<=max_value:
        word = str(j)
        counter=0
        if word[2]==word[5] and word[3]==word[4]:
            counter=counter+1
        else:
            j = j + 1
            continue

        word = str(j+1)
        if word[1]==word[5] and word[2]==word[4]:
            counter=counter+1
        else:
            j = j + 1
            continue

        word = str(j+2)
        if word[1]==word[4] and word[2]==word[3]:
            counter=counter+1
        else:
            j = j + 1
            continue

        word = str(j+3)
        if word[0]==word[5] and word[1]==word[4] and word[2]==word[3]:
            counter=counter+1
        else:
            j = j + 1
            continue

        if counter == 4:
            word = str(j)
            print(word)
        j = j + 1


show_possible_vals()