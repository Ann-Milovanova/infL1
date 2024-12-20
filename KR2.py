#лаба4№3
def t (matrix):
    t = 0
    for i in range(len(matrix)):
        t += matrix[i][i]
    return t
import random
A = [[random.randint(-10, 10) for _ in range(4)] for _ in range(4)]
print("Исходная матрица: ")
for i in A:
    print(i)
result = t(A)
print("След матрицы A:", result)

#лаба5№15
def find_average_without_extremes(matrix):
    f = [item for row in matrix for item in row]

    sorted_elements = sorted(f)

    elements_to_consider = sorted_elements[1:-1]

    average_value = sum(elements_to_consider) / len(elements_to_consider)

    return average_value

A = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
print("Исходная матрица А: ")
for i in A:
    print(i)

B = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
print("Исходная матрица В: ")
for i in B:
    print(i)

C = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
print("Исходная матрица C: ")
for i in C:
    print(i)

avg = []

avg.append(find_average_without_extremes(A))
avg.append(find_average_without_extremes(B))
avg.append(find_average_without_extremes(C))

print("Средние значения:", avg)

if all(avg[i] <= avg[i + 1] for i in range(len(avg) - 1)):
    print("Последовательность является возрастающей.")
elif all(avg[i] >= avg[i + 1] for i in range(len(avg) - 1)):
    print("Последовательность является убывающей.")
else:
    print("Последовательность не является ни убывающей, ни возрастающей.")
