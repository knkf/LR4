array = input("Введите элементы списка через пробел: ")
lst = list([int(array) for array in array.split()])
sizeList = []
for i in range(35, 50):
    if i not in sizeList and lst.count(i) != 0:
        sizeList.append([i, lst.count(i)])
for i in range(0, len(sizeList)):
    print("Кроссовки", sizeList[i][0], "размера в количестве:", sizeList[i][1])
