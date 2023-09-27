def gcd(a,b):
    while a%b!=0:
        c=a%b
        a=b
        b=c
    return b

x=int(input())
y=int(input())
print(gcd(max(x,y),min(x,y)))
