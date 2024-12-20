#ур1№1
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

# Ввод данных участников
participants = []
n = int(input("Введите количество участников: "))
for _ in range(n):
    name = input("Введите фамилию участника: ")
    society = input("Введите общество участника: ")
    attempt1 = float(input("Введите результат первой попытки: "))
    attempt2 = float(input("Введите результат второй попытки: "))
    participant = Participant(name, society, attempt1, attempt2)
    participants.append(participant)

# Сортировка участников по общему результату
bubble_sort(participants)

# Вывод результатов в виде таблицы
print("\nПротокол соревнований:")
print("{:<20} {:<20} {:<15} {:<15} {:<10}".format("Фамилия", "Общество", "Попытка 1", "Попытка 2", "Итого"))
print("-" * 85)
for participant in participants:
    print("{:<20} {:<20} {:<15} {:<15} {:<10}".format(participant.name, participant.society, participant.attempt1, participant.attempt2, participant.total_score))

#ур2№5
class Participant:
    def __init__(self, name, scores, jump_distance):
        self.name = name
        self.scores = scores
        self.jump_distance = jump_distance
        self.final_score = self.calculate_final_score()

    def calculate_final_score(self):
        # Сначала отбрасываем наименьшую и наибольшую оценки
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

        # Добавляем очки за дальность
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


# Ввод данных участников
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

# Сортировка участников по итоговому результату
bubble_sort(participants)

# Вывод результатов в виде таблицы
print("\nИтоговая таблица соревнований:")
print("{:<20} {:<10}".format("Фамилия", "Итоговый результат"))
print("-" * 30)
for participant in participants:
    print("{:<20} {:<10}".format(participant.name, participant.final_score))