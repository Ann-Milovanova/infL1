import math
a=0.1
b=1
h=0.1
e=0.0001
y=0
for x in range(1,11):
    i = 0
    x=x/10
    s = 999
    sum = 0
    y = math.cos(x)
    f = True
    while f:
        if abs(s)>e:
            s=(((-1)**i)*x**(2*i))/(math.factorial(2*i))
            sum=sum+s
            i = i + 1
            f=True
        else:
            sum = sum - s
            f=False
    print(sum,y)




