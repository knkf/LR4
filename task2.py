a = int(input("Введите значение первого члена прогрессии: "))
p = int(input("Введите разность арифметической прогрессии: "))
arithmeticProgression = []
for i in range(0, 10):
    if i == 0:
        arithmeticProgression.append(a)
    else:
        arithmeticProgression.append(arithmeticProgression[i-1] + p)
print(arithmeticProgression)

