import math

def fact(n,k):
    result = 1
    summ_val = n * k
    while True:
        if summ_val == 0:
            result = result*1
            break
        elif summ_val>0:
            result = result*summ_val
        summ_val=summ_val-1
    return result


def summ (n,k):
    sum_val = 0
    upper_part = 0
    lower_part = 0
    while True:
        if k<0:
            break
        else:
            upper_part = ((fact(n,k))*(1103+26390*k))
            lower_part = ((fact(1,k)**4))*(396**(4*k))
            sum_val = sum_val + upper_part/lower_part
            k = k - 1
    return sum_val

def composition(n,k):
    result = ((2*math.sqrt(2))/9801)*summ(n,k)
    return result




k = int(input("Please enter the K value > "))



if k>=0:
    pi_val = 1 / composition(4,k)
    print("PI is ",pi_val)
else:
    print("Please try to enter another values.")


