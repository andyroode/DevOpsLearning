import turtle

t = turtle.Turtle()


def koch(t,length):
    t.fd(length/3)
    t.lt(60)
    t.fd(length/3)
    t.rt(120)
    t.fd(length/3)
    t.lt(60)
    t.fd(length/3)



def snowflake(t,length):
    koch(t,length)
    t.lt(60)
    koch(t,length)
    t.rt(120)
    koch(t,length)
    t.lt(60)
    koch(t,length)
    t.lt(60)
    snowflake(t, length)
    t.lt(120)





length = int(input("Введите длину прямой: "))
snowflake(t,length)
turtle.mainloop()
