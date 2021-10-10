array17 = input("Введите список имён студентов 17 группы через запятую: ")
lst17 = list([array17 for array17 in array17.split(', ')])
array18 = input("Введите список имён студентов 18 группы через запятую: ")
lst18 = list([array18 for array18 in array18.split(', ')])
array19 = input("Введите список имён студентов 19 группы через запятую: ")
lst19 = list([array19 for array19 in array19.split(', ')])
minStudents = min(len(lst17), len(lst18), len(lst19))
group = 0
if len(lst17) == minStudents:
    group = 17
elif len(lst18) == minStudents:
    group = 18
else:
    group = 19
print("Самая малочисленная группа: ", group)
maxStudents = max(len(lst17), len(lst18), len(lst19))
if len(lst17) == maxStudents:
    group = 17
elif len(lst18) == maxStudents:
    group = 18
else:
    group = 19
print("Самая большая группа по составу: ", group)
ourGroup = lst17 + lst19 + lst18
ourGroup.sort()
print("Общий список студентов в трёх группах в алфавитном порядке: ")
for i in range(0, len(ourGroup)):
    print(str(i+1) + ".", ourGroup[i])
