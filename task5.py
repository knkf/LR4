from random import randrange


def array_sum(array):
    sum = 0;
    for element in array:
        sum += element
    return sum


lst = [randrange(25, 35) for i in range(42)]
print("Общее число учеников есть четырехзначное число? ", True if array_sum(lst) >= 1000 else False)
