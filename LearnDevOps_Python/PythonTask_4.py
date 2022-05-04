import turtle

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

polygon(t,5,100)