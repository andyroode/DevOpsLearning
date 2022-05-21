import math

def countdown(n):
    while n>0:
        print(n)
        n=n-1
    print("Done!")

##################################

def print_s(s,n):
    while n>=0:
        print(s)
        n=n-1

##################################

def Cycle_True(line):
    while True:
        line = input("> ")
        if line == ('Done!'):
            break
        print(line)
    print('Cycle is done!')


##################################

def Newton_func(x,a):
    y=0
    while y!=math.sqrt(a):
        y = (x+a/x)/2
        print(y)
        x=y

Newton_func(3,4)


