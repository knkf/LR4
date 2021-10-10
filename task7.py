from random import randrange
import random
mathEGE = [randrange(50, 101, 1) for i in range(100)]
rusEGE = [randrange(50, 101, 1) for i in range(100)]
infEGE = [randrange(50, 101, 1) for i in range(100)]
surnames = ["Быков", "Никитин", "Чумаков", "Денисов", "Медведев", "Плотников", "Волков",
            "Анисимов", "Леонов", "Гришин", "Казаков", "Николаев", "Чернов", "Кудрявцев",
            "Селиванов", "Лебедев", "Петров", "Баранов", "Анохин", "Свиридов"]
names = ["Михаил", "Андрей", "Фёдор", "Глеб", "Борис", "Алексей", "Святослав", "Юрий", "Платон", "Захар",
         "Лев", "Владимир", "Илья", "Николай", "Иван", "Евгений", "Матвей", "Максим", "Руслан", "Савелий"]
middleNames = ["Львович", "Георгиевич", "Матвеевич", "Станиславович", "Ярославович", "Игоревич", "Богданович",
               "Андреевич", "Алексеевич", "Дмитриевич", "Иванович", "Константинович", "Михайлович", "Викторович",
               "Николаевич", "Валерьевич", "Максимович", "Тимофеевич", "Сергеевич", "Егорович"]
pointsSum = []
for i in range(0, 100):
    pointsSum.append(mathEGE[i] + rusEGE[i] + infEGE[i])
applicants = []
for i in range(0, 100):
    enrollee = list()
    enrollee.append(pointsSum[i])
    enrollee.append(random.choice(surnames) + ' ' + random.choice(names) + ' ' + random.choice(middleNames))
    applicants.append(enrollee)
for i in range(1, 11):
    print(i, ":", applicants.pop(applicants.index(max(applicants)))[1])


