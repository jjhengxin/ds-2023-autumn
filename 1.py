import math
x=float(input())

z=int(x)
x=x-z


bz=[]
while z>=2:
    bz.append(z%2)
    z=z//2
bz.append(z%2)
for i in range(len(bz)): 
    print(bz[len(bz)-1-i],end="")


bx=[]
while x>0:
    bx.append(int(2*x))
    x=2*x-int(2*x)
if len(bx)>0:
    print(".",end="")
for i in range(len(bx)):
    print(bx[i],end="")
