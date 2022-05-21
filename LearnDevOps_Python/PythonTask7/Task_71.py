import math

def Newton_func(x,a):
    y=0
    while True:
        y = (x+a/x)/2
        if x == y:
            break
        x=y
    return y


def sqrt_compare(x,a):
    while a>0:
        print(a,"",Newton_func(x,a),"",math.sqrt(a),"",abs(math.sqrt(a)-Newton_func(x,a)))
        a = a - 1


sqrt_compare(6,18)

