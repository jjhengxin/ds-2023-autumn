import math

a1 = 0
def b1(n):
    return 1/(n*n)
def c1(x):
    return math.sqrt(x*6)

a2 = 0
def b2(n):
    return (-1)**(n+1)/(2*n-1)
def c2(x):
    return 4*x

a3 = 3
def b3(n):
    return (-1)**(n+1)*4/(2*n*(2*n+1)*(2*n+2))
def c3(x):
    return x

# a: 初始值
# b: 通项公式（函数）
# c: 后处理（函数）
# n: 累加项数
def f(a,b,c,n):
    z = a
    for i in range(n):
        z += b(i+1)
    return c(z)

print("%.10f"%f(a1,b1,c1,10000))
print("%.10f"%f(a2,b2,c2,10000))
print("%.10f"%f(a3,b3,c3,100))