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
    
№4ур1
def find_max_on_diagonal(matrix):
    max_element = matrix[0][0]
    max_index = 0
    for i in range(len(matrix)):
        if matrix[i][i] > max_element:
            max_element = matrix[i][i]
            max_index = i
    return max_element, max_index

def swap_row_column(A, B):
    max_A, row_index = find_max_on_diagonal(A)
    max_B, col_index = find_max_on_diagonal(B)

    for i in range(len(A)):
        A[row_index][i], B[i][col_index] = B[i][col_index], A[row_index][i]

    return A, B

import random
A = [[random.randint(-10, 10) for _ in range(5)] for _ in range(5)]

print("Матрица A:")
for row in A:
    print(row)

B = [[random.randint(-10, 10) for _ in range(5)] for _ in range(5)]
print("\nМатрица B:")
for row in B:
    print(row)

A, B = swap_row_column(A, B)

print("\nМатрица A после замены:")
for row in A:
    print(row)

print("\nМатрица B после замены:")
for row in B:
    print(row)

