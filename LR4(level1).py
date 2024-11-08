
#ур1№33 сформировать одномерный массив из отрицательных элементов матрицы А размером 5Х7
import random
A = [[random.randint(-10, 10) for _ in range(7)] for _ in range(5)]
print("Исходная матрица A:")
for r in A:
    print(r)
m=[]
for i in A:
    for j in i:
        if j>0:
            m.append(j)
print("Новый массив: ", m)
m=[]
for i in A:
    for j in i:
        if j>0:
            m.append(j)
print("Новый массив: ", m)
#ур2№2 Дана матрица A размера 7 × 5. Если количество положительных элементов столбца больше количества отрицательных, то максимальный элемент этого столбца заменить на 0, в противном случае максимальный элемент заменить на номер максимального элемента этого столбца
import random
A = [[random.randint(-10, 10) for _ in range(5)] for _ in range(7)]
print("Исходная матрица A:")
for r in A:
    print(r)
for c in range(5):
    positive_count = 0
    negative_count = 0
    max = A[0][c]
    max_index = 0
    for r in range(7):
        if A[r][c] > 0:
            positive_count += 1
        elif A[r][c] < 0:
            negative_count += 1
        if A[r][c] > max:
            max = A[r][c]
            max_index = r
    if positive_count > negative_count:
        A[max_index][c] = 0
    else:
        A[max_index][c] = max_index
print("Измененная матрица A:")
for r in A:
    print(r)
#ур3№2 Заполнить нулями элементы квадратной матрицы, расположенные по периметру (использовать один цикл)
import random
m = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
print("Исходная матрица A:")
for r in m:
    print(r)
l=0
for i in m:
    l=l+1
for i in range(len(m)):
    m[0][i]=0
    m[len(m)-1][i]=0
    m[i][0]=0
    m[i][len(m)-1]=0
print(m)
