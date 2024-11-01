
#ур1№33
a=[[1, 3, 5, -7, -8], [2, 3, -9, -8, 3]]
b=[]
for i in a:
    for j in i:
        if j>0:
            b.append(j)
print(b)
#ур2№
#ур3№2
m=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l=0
for i in m:
    l=l+1
for i in range(len(m)):
    m[0][i]=0
    m[len(m)-1][i]=0
    m[i][0]=0
    m[i][len(m)-1]=0
print(m)
