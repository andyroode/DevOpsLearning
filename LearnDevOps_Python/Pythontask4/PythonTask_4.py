import turtle
import math

t=turtle.Turtle()

def square(t_name,length):
    t_name.pd()
    t_name.fd(length)
    t_name.lt(90)
    t_name.fd(length)
    t_name.lt(90)
    t_name.fd(length)
    t_name.lt(90)
    t_name.fd(length)
    turtle.mainloop()


def polygon(t_name,length,n):
    t_name.pd()
    for i in range(n):
        t_name.fd(length)
        t_name.lt(360/n)
    turtle.mainloop()




def circle(t_name,r):
    circumreference = 2*math.pi*r
    length = 1
    n = circumreference / length
    t_name.up()
    #t_name.fd(r)
    t_name.lt(360/n)
    polygon(t_name,length,int(n))


def arc(t_name,r,angle):
    circumreference = 2*math.pi*r*(angle/360)
    length = 3
    n = circumreference / length
    t_name.up()
    t_name.fd(r)
    t_name.lt(360/n)
    t_name.pd()
    for i in range(int(n)):
        t_name.fd(circumreference/n)
        t_name.lt(angle/n)
    turtle.mainloop()


polygon(t, 50, 7)
