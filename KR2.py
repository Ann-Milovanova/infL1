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

class Participant:
    def __init__(self, name, result):
        self.name = name
        self.result = result

def bubble_sort(participants):
    n = len(participants)
    for i in range(n):
        for j in range(n - 1 - i):
            if participants[j].result > participants[j + 1].result: 
                participants[j], participants[j + 1] = participants[j + 1], participants[j]

def input_participants(group_name):
    participants = []
    n = int(input(f"Введите количество участников для группы {group_name}: "))
    for _ in range(n):
        name = input("Введите фамилию участника: ")
        result = float(input("Введите результат участника: "))
        participant = Participant(name, result)
        participants.append(participant)
    return participants

def main():

    group1_participants = input_participants("1")
    group2_participants = input_participants("2")

    bubble_sort(group1_participants)
    bubble_sort(group2_participants)

    combined_participants = group1_participants + group2_participants

    bubble_sort(combined_participants)

    print("\nИтоговая таблица соревнований:")
    print("{:<20} {:<10}".format("Фамилия", "Результат"))
    print("-" * 30)
    for participant in combined_participants:
        print("{:<20} {:<10}".format(participant.name, participant.result))

if __name__ == "__main__":
    main()
    print("{:<20} {:<10}".format(name, result))
