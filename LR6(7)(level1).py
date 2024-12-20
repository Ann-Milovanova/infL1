#ур1№1 Результаты соревнований по прыжкам в длину определяются по сумме двух попыток. В протоколе для каждого участника указываются: фамилия, общество, результаты первой и второй попыток. Вывести протокол в виде таблицы с заголовком в порядке занятых мест.
class Participant:
    def __init__(self, name, society, attempt1, attempt2):
        self.name = name
        self.society = society
        self.attempt1 = attempt1
        self.attempt2 = attempt2
        self.total_score = self.calculate_total_score()

    def calculate_total_score(self):
        return self.attempt1 + self.attempt2

def bubble_sort(participants):
    n = len(participants)
    for i in range(n):
        for j in range(n - 1 - i):
            if participants[j].total_score < participants[j + 1].total_score:
                participants[j], participants[j + 1] = participants[j + 1], participants[j]

participants = []
n = int(input("Введите количество участников: "))
for _ in range(n):
    name = input("Введите фамилию участника: ")
    society = input("Введите общество участника: ")
    attempt1 = float(input("Введите результат первой попытки: "))
    attempt2 = float(input("Введите результат второй попытки: "))
    participant = Participant(name, society, attempt1, attempt2)
    participants.append(participant)

bubble_sort(participants)

print("\nПротокол соревнований:")
print("{:<20} {:<20} {:<15} {:<15} {:<10}".format("Фамилия", "Общество", "Попытка 1", "Попытка 2", "Итого"))
print("-" * 85)
for participant in participants:
    print("{:<20} {:<20} {:<15} {:<15} {:<10}".format(participant.name, participant.society, participant.attempt1, participant.attempt2, participant.total_score))

#ур2№5 Соревнования по прыжкам на лыжах со 120-метрового трамплина оценивают 5 судей. Каждый судья выставляет оценку за стиль прыжка по 20-балльной шкале. Меньшая и большая оценки отбрасываются, остальные суммируются. К этой сумме прибавляются очки за дальность прыжка: 120 м – 60 очков, за каждый метр превышения добавляются по 2 очка, при меньшей дальности отнимаются 2 очка за каждый метр. Получить итоговую таблицу соревнований, содержащую фамилию и итоговый результат для каждого участника в порядке занятых мест.
class Participant:
    def __init__(self, name, scores, jump_distance):
        self.name = name
        self.scores = scores
        self.jump_distance = jump_distance
        self.final_score = self.calculate_final_score()

    def calculate_final_score(self):
        
        min_score = max_score = self.scores[0]

        for score in self.scores:
            if score < min_score:
                min_score = score
            if score > max_score:
                max_score = score

        total_style_score = 0
        for score in self.scores:
            if score != min_score and score != max_score:
                total_style_score += score
                
        if self.jump_distance > 120:
            total_style_score += 60 + (self.jump_distance - 120) * 2
        else:
            total_style_score += 60 - (120 - self.jump_distance) * 2

        return total_style_score


def bubble_sort(participants):
    n = len(participants)
    for i in range(n):
        for j in range(n - 1 - i):
            if participants[j].final_score < participants[j + 1].final_score:
                participants[j], participants[j + 1] = participants[j + 1], participants[j]

participants = []
n = int(input("Введите количество участников: "))
for _ in range(n):
    name = input("Введите фамилию участника: ")
    scores = []
    for i in range(5):
        score = int(input(f"Введите оценку судьи {i + 1} (0-20): "))
        scores.append(score)
    jump_distance = float(input("Введите дальность прыжка (в метрах): "))
    participant = Participant(name, scores, jump_distance)
    participants.append(participant)

bubble_sort(participants)

print("\nИтоговая таблица соревнований:")
print("{:<20} {:<10}".format("Фамилия", "Итоговый результат"))
print("-" * 30)
for participant in participants:
    print("{:<20} {:<10}".format(participant.name, participant.final_score))

#ур3№1 Результаты сессии содержат оценки 5 экзаменов по каждой группе. Определить средний балл для трех групп студентов одного потока и выдать список групп в порядке убывания среднего балла. Результаты вывести в виде таблицы с заголовком.
class Group:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.average_score = self.calculate_average_score()

    def calculate_average_score(self):
        total_score = 0
        for score in self.scores:
            total_score += score
        return total_score / len(self.scores)

def bubble_sort(groups):
    n = len(groups)
    for i in range(n):
        for j in range(n - 1 - i):
            if groups[j].average_score < groups[j + 1].average_score:
                groups[j], groups[j + 1] = groups[j + 1], groups[j]

groups = []
n = 3  
for _ in range(n):
    name = input("Введите название группы: ")
    scores = []
    for i in range(5):
        score = float(input(f"Введите оценку за экзамен {i + 1}: "))
        scores.append(score)
    group = Group(name, scores)
    groups.append(group)

bubble_sort(groups)

print("\nИтоговая таблица средних баллов по группам:")
print("{:<20} {:<10}".format("Группа", "Средний балл"))
print("-" * 30)
for group in groups:
    print("{:<20} {:<10.2f}".format(group.name, group.average_score))
