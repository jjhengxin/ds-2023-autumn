import math
n=int(input())
check=True

for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
        check=False
        break
print(check)