array = input("Введите элементы списка через пробел: ")
lst = [int(array) for array in array.split()]
evenNumbers = []
endZeroNumbers = []
for element in lst:
    if element % 2 == 0:
        evenNumbers.append(element)
        if element % 10 == 0:
            endZeroNumbers.append(element)
print("а)", evenNumbers)
print("б)", endZeroNumbers)
