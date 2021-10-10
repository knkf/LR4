def array_sum(sequence):
    sum = 0
    for element in sequence:
        sum += element
    return sum


array = input("Введите элементы списка через запятую: ")
lst = list([int(array) for array in array.split(', ')])
print("Средний балл Васи:", array_sum(lst) / len(lst))
result = ""
for i in range(0, len(lst)):
    if i == len(lst) - 1:
        result += str(lst[i]) + ". "
    else:
        result += str(lst[i]) + "; "
print("Оценки Васи:", result)
