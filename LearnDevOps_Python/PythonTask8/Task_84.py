def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


print(any_lowercase1("Hello"))
#Функция проверяет, все ли буквы строчные


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

print(any_lowercase2("Hello"))
#Функция проверяет, является ли буква с строчной


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

print(any_lowercase3("HellO"))
#Функция идет по всем индексам строки, проверяет значение последнего индекса - строчная или заглавная

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

print(any_lowercase4("HELLO"))
#Функция идет по всем индексам строки. Если находит хотя бы одну строчную букву, присуждает флагу значение true.


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


print(any_lowercase5("helLo"))
#Функция идет по всем индексам и если находит заглавную букву то возвращает False.
