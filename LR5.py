№2ур1
print('Введите длины сторон треугольников ')
from math import sqrt
a1=int(input())
b1=int(input())
c1=int(input())
a2=int(input())
b2=int(input())
c2=int(input())
p1=(a1+b1+c1)/2
def s1 (a1, b1, c1, p1):
    return sqrt(p1*(p1-a1)*(p1-b1)*(p1-c1))
result1=(a1, b1, c1)
def s2(a2, b2, c2, p2):
    return sqrt(p2*(p2-a2)*(p2-b2)*(p2-c2))
result2=(a2, b2, c2)
if result1>result2:
    print('Первый треугольник больше ')
if result1<result2:
    print('Второй треугольник больше ')
    
№24ур1
import random
A = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
B = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
print('Ваши матрицы: ', A, B)
d_A = [A[i][i] for i in range(len(A))]
d_B = [B[i][i] for i in range(len(B))]
print(d_A, d_B)
def 

