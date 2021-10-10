array = input("Введите список: ")
lst = list([array for array in array.split("], [")])
lst[0] = lst[0].replace("[[", "")
lst[len(lst)-1] = lst[len(lst)-1].replace("]]", "")
result = []
for element in lst:
    sequence = list(element for element in element.split(", "))
    result.append(int(sequence[0]))
    result.append(int(sequence[1]))
print(result)
