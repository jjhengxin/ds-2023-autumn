x=float(input())
l=0
r=x

for i in range(15):
    mid=(l+r)/2
    if mid*mid*mid==x: break
    if mid*mid*mid<x: l=mid
    else :r=mid
t=round(mid)
if t*t*t==x: print(t)
else: print(mid)