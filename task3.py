def array_reverse(sequence):
    output = []
    for i in range(len(sequence) - 1, -1, -1):
        output.append(sequence[i])
    return output


array = input("Введите элементы списка через пробел: ")
lst = [int(array) for array in array.split()]
print(array_reverse(lst))
