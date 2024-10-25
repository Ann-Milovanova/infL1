from random import randint
print(randint(1, 33))
print(randint(1, 9))
print(randint(1, 14))

#ур1№33
a=[[1, 3, 5, -7, -8], [2, 3, -9, -8, 3]]
b=[]
for i in a:
    for j in i:
        if j>0:
            b.append(j)
print(b)

