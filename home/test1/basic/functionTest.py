import math
def quadratic(a,b,c):
    x = (b**2 - 2*a*c)/(2*a)
    print(x)

quadratic(4,2,1)

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5,2))

