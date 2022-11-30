def find_remainder(val1,val2):
   if val1==val2:
        r = 0
   else:
       r=val1%val2
       return r

def find_min_remainder(val1,val2):
    init_remainder = find_remainder(val1,val2)
    if init_remainder == 0:
        return val2
    else:
        min_remainder = find_remainder(val1,init_remainder)
        if min_remainder == 0:
            return init_remainder
        else:
            return find_min_remainder(init_remainder,min_remainder)


def gdc(val1,val2):
    if val1>val2:
        return find_min_remainder(val1,val2)
    else:
        return find_min_remainder(val2,val1)



val1 = int(input("Please enter the first value:\n"))
val2 = int(input("Please enter the second value:\n"))
print("Greatest common divisor is",gdc(val1,val2))



