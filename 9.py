def f(i):
    ret=1
    for j in range(n):
        if j!=i:
            ret*=a[j]
    return ret

n=int(input())
a=[]
b=[]
a=list(map(int,input().split()))

for i in range(n):
    b.append(f(i))
print(b)
