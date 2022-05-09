#Значение N должно быть больше или равно нулю, иначе будет бесконечная рекурсия.

def recurse(n,s):
    if n==0:
        print(s)
    else:
        recurse(n-1,n+s)

recurse(0,0)