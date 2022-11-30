def is_power(a,b):
    if a%b==0 and (a/b)%b==0:
        return True
    else:
        return False



if is_power(4,3):
    print("TRUE")
else:
    print("FALSE")