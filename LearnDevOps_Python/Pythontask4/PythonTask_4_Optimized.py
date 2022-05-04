import turtle
import math

t=turtle.Turtle()

def square(t_name,length):
    t_name.pd()
    for i in range(4):
        t_name.fd(length)
        t_name.lt(90)

    turtle.mainloop()

def circle (t_name, r, angle):
    arc(t_name, r, angle) #Используем функцию arc для отрисовки окружности. Угол задаем 360 для окружности и меньше для дуги
    turtle.mainloop()

def arc(t_name,r,angle):  #базовая функция для арки. Если Angle = 360 то на выходе будет окружность.
    circumreference = 2*math.pi*r*(angle/360)
    length = 3
    n = circumreference / length #количество сторон многоугольника, который будет рисовать окружность
    t_name.pd()
    len_step = circumreference / n
    angle_step = angle / n
    polyline(t_name,len_step,angle_step,n)

def polyline(t_name, length, angle, n):
    for i in range(int(n)):
        t_name.fd(length)
        t_name.lt(angle)


circle(t, 100,45)