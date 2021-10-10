array = input("Введите список имён гостей через запятую: ")
lst = list([array for array in array.split(', ')])
count = 0
for i in range(0, len(lst)):
    if i == len(lst)-1:
        break
    if lst[i] == lst[i+1]:
        count += 1
print("Количество пар гостей с одинаковыми именами: ", count)
