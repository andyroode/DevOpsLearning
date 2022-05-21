import math
import turtle

def hypotenuse(a,b):
    print("Катет a равен",a)
    print("Катет b равен",b)
    sqr_val = a**2 + b**2
    print("Сумма квадратов катетов равна",sqr_val)
    c = math.sqrt(sqr_val)
    print("Длина гипотенузы треугольника равна",c)
    return 0

hypotenuse(7,19)