#ур1№9
x=int(input())
if x<=-1:
    y=0
    print(y)
elif -1<x<=0:
    y=1+x
    print(y)
elif x>0:
    y=1
    print(y)
#ур2№3
n=int(input('Введите количество спортсменов '))
a=[]
while n !=0:
    s=int(input('Введите результат '))
    n=n-1
    a.append(s)
    mn=10**8
for i in range(len(a)):
    mn = min(mn, a[i])
print('лучший: ',mn)