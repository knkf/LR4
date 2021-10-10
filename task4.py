def array_sum(array):
    sum = 0;
    for element in array:
        sum += element
    return sum


array = input("Введите элементы списка через пробел: ")
lst = [int(array) for array in array.split()]
evenNumbers = []
oddNumbers = []
for i in range(1, len(lst), 2):
    evenNumbers.append(lst[i])
for i in range(0, len(lst), 2):
    oddNumbers.append(lst[i])
print("Знакопеременная сумма равна:", array_sum(oddNumbers) - array_sum(evenNumbers))
