s=input()
check=False
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        check=True
if check:
    print("YES")
else: print("NO")
