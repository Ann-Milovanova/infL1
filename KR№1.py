#ур1№16
n=64
b=1
q=2
s=0
for i in range(1, n):
    s=b*(q**n-1)/(q-1)
    s=s/15
    d=round(s)
print(d)

#ур2№5
n=1
h=0
print ("Введите норматив")
b = input()
print ("Введите результат")
while (n<=30):
    n=n+1
    k= input()
    if (k<=b):
        h=h+1
print("в финале спортсменов ", h)

#ур3№12
arr = [5, -3, 8, -1, 0, 7, -6, 4, -9, 2, -8, 6]
arr = [x for x in arr if x >= 0]
print(arr)
