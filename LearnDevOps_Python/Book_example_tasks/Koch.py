import math
import turtle

leo = turtle.Turtle()

def koch_line(t,length):
    t.fd(length/3)
    t.lt(60)
    t.fd(length/3)
    t.rt(120)
    t.fd(length/3)
    t.lt(60)
    t.fd(length/3)


def koch_line_n(t,length):
    koch_line(t,length)
    t.lt(60)
    koch_line(t,length)
    t.rt(120)
    koch_line(t,length)
    t.lt(60)
    koch_line(t,length)
    t.lt(60)












leo.pu()
leo.lt(180)
leo.fd(200)
leo.lt(180)
leo.pd()
koch_line_n(leo,100)
turtle.mainloop()

