import math
import turtle

t = turtle.Turtle()


def circumRadius(length, n):
    r = length/float(2*math.sin(360/2*n))
    return r

def side_a(length, r):
    a = math.sqrt(r**2 - (0.5*length)**2)
    return a

def find_angle(a,c):
    angle = math.degrees(math.sin(a/c))
    return angle

def printPolygon(t_name,length,n):

    radius = circumRadius(length, n)
    a = side_a(length,radius)
    lt_angle = find_angle(a,radius)
    for i in range(n):
        t_name.fd(length)
        t_name.lt(lt_angle)
        t_name.fd(radius)
        t_name.lt(180-2*lt_angle)
        t_name.fd(radius)
        t_name.pu()
        t_name.lt(lt_angle)
        t_name.fd(length)
        t_name.pd()

printPolygon(t,50,5)
turtle.mainloop()