lst = []
for i in range(1, 10001):
    if (i % 3 == 0 and i % 7 == 0) or i % 9 == 0:
        lst.append(i)
print(lst)

# ПЕРЕДЕЛАТЬ С ИСПОЛЬЗОВАНИЕ ГЕНЕРАТОРА
