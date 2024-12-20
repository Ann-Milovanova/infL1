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

#лаба6(7) №4
class Participant:
    def init(self, surname, result):
        self.surname = surname
        self.result = result

    def repr(self):
        return f"{self.surname}: {self.result}"


class SkiRaceGroup:
    def init(self, name):
        self.name = name
        self.participants = []

    def add_participant(self, surname, result):
        participant = Participant(surname, result)
        self.participants.append(participant)

    def sort_results(self):
        self.participants.sort(key=lambda x: x.result)

    def str(self):
        return f"Group: {self.name}\n" + "\n".join(f"{index + 1}. {participant.surname} - {participant.result}" 
                                                     for index, participant in enumerate(self.participants))


class SkiRace:
    def init(self):
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)

    def display_results(self):
        print("Соревнования по лыжным гонкам")
        print("=" * 30)
        for group in self.groups:
            group.sort_results()
            print(group)
            print("-" * 30)


# Пример использования
if name == "main":
    group1 = SkiRaceGroup("Группа 1")
    group1.add_participant("Иванов", 15)
    group1.add_participant("Петров", 10)
    group1.add_participant("Сидоров", 12)

    group2 = SkiRaceGroup("Группа 2")
    group2.add_participant("Кузнецов", 9)
    group2.add_participant("Смирнов", 14)
    group2.add_participant("Попов", 11)

    ski_race = SkiRace()
    ski_race.add_group(group1)
    ski_race.add_group(group2)

    ski_race.display_results()


