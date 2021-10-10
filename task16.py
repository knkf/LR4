n = int(input("Введите число n: "))
lst = [str(i)+str(i) for i in range(1, n+1)]
for element in lst:
    print(element)