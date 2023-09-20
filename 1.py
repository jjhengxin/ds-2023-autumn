n=int(input())
ans=1
if n<=3 : 
    print(n-1)
else:
    if n%3==1:
        n=n-4
        ans=4
        for i in range(n//3):
            ans*=3
            print("3",end=",")
        print("4")
    else:
        if n%3==2:
            print("2",end=",")
            ans=2
        for i in range(n//3-1):
            ans*=3
            print("3",end=",")
        ans*=3
        print("3")

print (ans)