import math
import turtle

t = turtle.Turtle()


def circumRadius(length, n):
    r = length/float(2*math.sin(math.pi/n))
    return r



def find_angle(n):
    high_angle = 360/n
    angle = (180 - high_angle) / 2
    return angle

def printPolygon(t_name,length,n):
    #t_name.hideturtle()
    radius = circumRadius(length, n)
    lt_angle = find_angle(n)
    for i in range(n):
        t_name.fd(length)
        t_name.lt(180-lt_angle)
        t_name.fd(radius)
        t_name.lt(180-(360/n))
        t_name.fd(radius)
        t_name.pu()
        t_name.lt(180-lt_angle)
        t_name.fd(length)
        t_name.lt(360/n)
        t_name.pd()

printPolygon(t,200,5)
turtle.mainloop()