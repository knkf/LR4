lst = [i + 2 for i in range(1, 21, 2)]
lst1 = [i ** 2 for i in range(2, 21, 2)]
result = []
for i in range(0, 10):
    result.append(lst[i])
    result.append(lst1[i])
print(result)
