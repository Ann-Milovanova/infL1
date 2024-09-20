import math
a=0.1
b=1
i=0
sum=0
h=0.1
e=0.0001
s=999
y=0
for x in range(1,11):
    x=x/10
    while abs(s)>e:
        y=math.cos(x)
        s=(((-1)**i)*x**(2*i))/(math.factorial(2*i))
        sum=sum+s
        i = i + 1
    else:
        sum = sum - s
    print(sum,y)



