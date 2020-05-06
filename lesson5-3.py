# ДЕсть список объектов. Нужно посчитать сколько раз какой тип данных встречается в списке.
#
# [1, 'one', 'two', 3.0, 4j, 5j, 3, 2, 12., 17, [1,2], {1:1}]
# И вывести только объекты самого частого типа
import random
listik = [1, 'one', 'two', 'three', 'four', 3.0, 4j, 5j, 3, 2, 12., 17, [1,2], {1:1}]
slovarik = {}
for i in listik:
    slovarik[type(i)] = slovarik.get(type(i), 0) + 1
print(slovarik)
count = 0
for i in slovarik:
    if slovarik[i] > count:
        count = count + slovarik[i]
for i in slovarik:
    if slovarik[i] == count:
        for k in listik:
            if type(k) == i:
                print(k)