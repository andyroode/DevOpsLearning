import math
import turtle

def return_check(x,y):
    if x>y:
        return 1
    elif x==y:
        return 0
    elif x<y:
        return -1



def distance(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    print("Значение dx =",dx)
    print("Значение dy =",dy)

    dsquared = dx**2 + dy**2
    print("Сумма квадратов равна ",dsquared)

    length = math.sqrt(dsquared)
    print("Длина прямой равна",length)
    return 0

distance(2,3,8,7)