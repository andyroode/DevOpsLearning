import math
import turtle

t=turtle.Turtle()

def circle (t_name, r, angle):
    arc(t_name, r, angle) #Используем функцию arc для отрисовки окружности. Угол задаем 360 для окружности и меньше для дуги


def arc(t_name,r,angle):  #базовая функция для арки. Если Angle = 360 то на выходе будет окружность.
    circumreference = 2*math.pi*r*float(angle/360)
    length = 3
    n = circumreference / length #количество сторон многоугольника, который будет рисовать окружность
    t_name.pd()
    len_step = float(circumreference / n)
    angle_step = float(angle / n)
    polyline(t_name,len_step,angle_step,n)

def polyline(t_name, length, angle, n):
    for i in range(int(n)):
        t_name.fd(length)
        t_name.lt(angle)


def flower(t_name, r, angle, count):
    for i in range(count):

        circle(t_name,r,angle)
        t_name.lt(180-angle)
        circle(t_name,r,angle)
        t.home()
        t_name.lt(float((i+1)*float(360/count)))
    t_name.hideturtle()



flower(t,300,40,8)
turtle.mainloop()