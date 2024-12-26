#ур1№1 Результаты соревнований по прыжкам в длину определяются по сумме двух попыток. В протоколе для каждого участника указываются: фамилия, общество, результаты первой и второй попыток. Вывести протокол в виде таблицы с заголовком в порядке занятых мест.

 class Athlete:
    def __init__(self, surname, society, attempt1, attempt2):
        self.surname = surname
        self.society = society
        self.attempt1 = attempt1
        self.attempt2 = attempt2
        self.total_score = self.calculate_total_score()

    def calculate_total_score(self):
        return self.attempt1 + self.attempt2

class Competition:
    def __init__(self):
        self.athletes = []

    def add_athlete(self, surname, society, attempt1, attempt2):
        athlete = Athlete(surname, society, attempt1, attempt2)
        self.athletes.append(athlete)

    def get_results(self):

        n = len(self.athletes)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.athletes[j].total_score < self.athletes[j+1].total_score:
                    self.athletes[j], self.athletes[j+1] = self.athletes[j+1], self.athletes[j]

    def print_protocol(self):
        self.get_results()
        print(f"{'Место':<6} {'Фамилия':<15} {'Общество':<15} {'Сумма попыток':<15}")
        print("-" * 60)
        for place in range(len(self.athletes)):
            athlete = self.athletes[place]
            print(f"{place + 1:<6} {athlete.surname:<15} {athlete.society:<15} {athlete.total_score:<15}")

competition = Competition()
competition.add_athlete("Милованова", "Аниме", 6.5, 7.2)
competition.add_athlete("Билявский", "Мультфильмы", 7.0, 6.8)
competition.add_athlete("Федотова", "Книги", 6.9, 7.5)

competition.print_protocol()

#ур2№5 Соревнования по прыжкам на лыжах со 120-метрового трамплина оценивают 5 судей. Каждый судья выставляет оценку за стиль прыжка по 20-балльной шкале. Меньшая и большая оценки отбрасываются, остальные суммируются. К этой сумме прибавляются очки за дальность прыжка: 120 м – 60 очков, за каждый метр превышения добавляются по 2 очка, при меньшей дальности отнимаются 2 очка за каждый метр. Получить итоговую таблицу соревнований, содержащую фамилию и итоговый результат для каждого участника в порядке занятых мест.

  class Athlete:
    def __init__(self, name, scores, distance):
        self.name = name
        self.scores = scores
        self.distance = distance
        self.final_score = self.calculate_final_score()

    def calculate_final_score(self):
        min_score = self.scores[0]
        max_score = self.scores[0]
        total_score = 0

        for score in self.scores:
            if score < min_score:
                min_score = score
            if score > max_score:
                max_score = score

        for score in self.scores:
            if score != min_score and score != max_score:
                total_score += score

        if self.distance > 120:
            distance_points = 60 + (self.distance - 120) * 2
        else:
            distance_points = 60 - (120 - self.distance) * 2

        return total_score + distance_points


class Competition:
    def __init__(self):
        self.athletes = []

    def add_athlete(self, name, scores, distance):
        athlete = Athlete(name, scores, distance)
        self.athletes.append(athlete)

    def get_results(self):

        n = len(self.athletes)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.athletes[j].final_score < self.athletes[j + 1].final_score:
                    self.athletes[j], self.athletes[j + 1] = self.athletes[j + 1], self.athletes[j]

        results = []
        for athlete in self.athletes:
            results.append((athlete.name, athlete.final_score))
        return results


competition = Competition()
competition.add_athlete("Федотова", [18, 19, 20, 17, 16], 125)
competition.add_athlete("Милованова", [20, 20, 19, 18, 19], 118)
competition.add_athlete("Билявский", [15, 16, 18, 17, 14], 130)

results = competition.get_results()
for place in range(len(results)):
    name, score = results[place]
    print(f"{place + 1}. {name}: {score}")


#ур3№1 Результаты сессии содержат оценки 5 экзаменов по каждой группе. Определить средний балл для трех групп студентов одного потока и выдать список групп в порядке убывания среднего балла. Результаты вывести в виде таблицы с заголовком.

         class Group:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.average_score = self.calculate_average()

    def calculate_average(self):
        total = 0
        for score in self.scores:
            total += score
        return total / len(self.scores) if self.scores else 0

class Session:
    def __init__(self):
        self.groups = []

    def add_group(self, name, scores):
        group = Group(name, scores)
        self.groups.append(group)

    def sort_groups(self):
        n = len(self.groups)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.groups[j].average_score < self.groups[j+1].average_score:
                    self.groups[j], self.groups[j+1] = self.groups[j+1], self.groups[j]

    def print_results(self):
        self.sort_groups()
        print(f"{'Группа':<15} {'Средний балл':<15}")
        print("-" * 30)
        for group in self.groups:
            print(f"{group.name:<15} {group.average_score:<15.2f}")

session = Session()
session.add_group("Группа Наноматериалы", [4, 5, 3, 4, 5])
session.add_group("Группа Материаловеды", [3, 4, 3, 2, 4])
session.add_group("Группа БФЗ-24-1", [5, 5, 5, 5, 5])

session.print_results()
