array = input("Введите элементы списка через пробел: ")
lst = [int(array) for array in array.split()]
different = []
for element in lst:
    if element not in different:
        different.append(element)
print("Число различных элементов: ", len(different))
