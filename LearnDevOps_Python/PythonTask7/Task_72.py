import math
def eval_loop():
    last_val = 'Nothing yet!'
    while True:
        n = input('> ')
        if n=='Done':
            print(last_val)
            break
        last_val = eval(n)



eval_loop()