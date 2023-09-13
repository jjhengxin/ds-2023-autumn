myli = [int(num_str) for num_str in input().split()]
lilen = len(myli)

myli2=[]
for i in range(lilen):
    myli2.append(myli[lilen-1-i])
print(myli2)

myli3=[]
k=0
while k<lilen:
    myli3.append(myli[lilen-k-1])
    k+=1
print(myli3)