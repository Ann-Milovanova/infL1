#№2ур1 Два треугольника заданы длинами своих сторон a, b, c. Определить треугольник с большей площадью, вычисляя площади по формуле Герона 
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
    
#№4ур1 Поменять местами строку матрицы А размером 5х5 и столбец матрицы В размером 5х5, содержащие максимальные элементы на диагоналях
def max_diag(matrix):
    mx = matrix[0][0]
    mx_ind = 0
    for i in range(len(matrix)):
        if matrix[i][i] > mx:
            mx = matrix[i][i]
            mx_ind = i
    return mx, mx_ind

def s (A, B):
    max_A, row_index = max_diag(A)
    max_B, col_index = max_diag(B)

    for i in range(len(A)):
        A[row_index][i], B[i][col_index] = B[i][col_index], A[row_index][i]

    return A, B

import random
A = [[random.randint(-10, 10) for _ in range(5)] for _ in range(5)]

print("Матрица A:")
for i in A:
    print(i)

B = [[random.randint(-10, 10) for _ in range(5)] for _ in range(5)]
print("Матрица B:")
for i in B:
    print(i)

A, B = s(A, B)

print("Матрица A после замены:")
for i in A:
    print(i)

print("Матрица B после замены:")
for i in B:
    print(i)

#№2ур3 В заданной матрице расположить элементы чётных строк в порядке возрастания, а элементы нечётных строк - в порядке убывания. 
def sort_matrix(matrix):
    def sort_row(row, ascending=True):
        return sorted(row, reverse=not ascending)

    for index, row in enumerate(matrix):
        if index % 2 == 0:
            matrix[index] = sort_row(row, ascending=True)
        else:
            matrix[index] = sort_row(row, ascending=False)

    return matrix

import random
matrix = [[random.randint(-10, 10) for _ in range(5)] for _ in range(5)]
print("Матрица:")
for i in matrix:
    print(i)
sorted_matrix = sort_matrix(matrix)
print("Изменённая матрица: ")
for i in sorted_matrix:
    print(i)
