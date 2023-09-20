import random 
import math
def f(times):
    sum = 0
    for i in range(times):
        x=random.uniform(2,3)
        y=random.uniform(0,21)
        d=x*x+4*x*math.sin(x)-y
        if d>0:
            sum+=1
    return sum*21/times
print(f(1000000))
print(19/3+4*( math.sin(3)-3*math.cos(3) -math.sin(2) + 2*math.cos(2)))