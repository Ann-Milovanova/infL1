#лаба4№3 Найти след (сумму диагональных элементов) квадратной матрицы А размером 4 × 4).
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

#лаба5№15 Для каждой из трех заданных матриц найти среднее значение ее элементов без учета максимального и минимального элементов. Полученные значения занести в одномерный массив. Определить, образовали ли полученные значения убывающую или возрастающую последовательность. Нахождение среднего значения элементов матрицы оформить в вид метода.
def calculate_average(matrix):
    f = [item for row in matrix for item in row]  
    if len(f) <= 2: 
        return None
    
    max_value = max(f)  
    min_value = min(f)  
    
    filtered_list = [x for x in f if x != max_value and x != min_value]
    
    if len(filtered_list) == 0:
        return None
    
    average = sum(filtered_list) / len(filtered_list)  
    return average
    
import random 

matrix1 = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
print("Исходная матрица 1: ")
for i in matrix1:
    print(i)

matrix2 = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
print("Исходная матрица 2: ")
for i in matrix2:
    print(i)

matrix3 = [[random.randint(-10, 10) for _ in range(3)] for _ in range(3)]
print("Исходная матрица 3: ")
for i in matrix3:
    print(i)


averages = []
averages.append(calculate_average(matrix1))
averages.append(calculate_average(matrix2))
averages.append(calculate_average(matrix3))

def is_increasing(seq):
    return all(x < y for x, y in zip(seq, seq[1:]))

def is_decreasing(seq):
    return all(x > y for x, y in zip(seq, seq[1:]))

averages = [avg for avg in averages if avg is not None]

if is_increasing(averages):
    sequence_type = "возрастающая"
elif is_decreasing(averages):
    sequence_type = "убывающая"
else:
    sequence_type = "не является ни возрастающей, ни убывающей"

print("Средние значения:", averages)
print("Полученные значения образуют:", sequence_type, "последовательность.")

#лаба6(7) №4 Лыжные гонки проводятся отдельно для двух групп участников. Результаты соревнований заданы в виде фамилий участников и их результатов в каждой группе. Расположить результаты соревнований в каждой группе в порядке занятых мест. Объединить результаты обеих групп с сохранением упорядоченности и вывести в виде таблицы с заголовком.

group1 = []
n1 = int(input("Введите количество участников в первой группе: "))
for _ in range(n1):
    name, result = input("Введите фамилию участника и его результат (через пробел): ").split()
    group1.append((name, int(result)))
                  
group2 = []
n2 = int(input("Введите количество участников во второй группе: "))
for _ in range(n2):
    name, result = input("Введите фамилию участника и его результат (через пробел): ").split()
    group2.append((name, int(result)))

group1.sort(key=lambda x: x[1])
group2.sort(key=lambda x: x[1])

combined_results = group1 + group2

combined_results.sort(key=lambda x: x[1])

print("\nРезультаты соревнований:")
print("{:<20} {:<10}".format("Фамилия", "Результат"))
print("-" * 30)
for name, result in combined_results:
    print("{:<20} {:<10}".format(name, result))
