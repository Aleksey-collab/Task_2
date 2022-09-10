# Петя впервые пришел на урок физкультуры в новой школе. Перед началом урока ученики выстраиваются по росту, 
# в порядке невозрастания. Напишите программу, которая определит на какое место в шеренге Пете нужно встать, 
# чтобы не нарушить традицию, если заранее известен рост каждого ученика и эти данные уже расположены по невозрастанию 
# (то есть каждое следующее число не больше предыдущего). Если в классе есть несколько учеников с таким же ростом, 
# как у Пети, то программа должна расположить его после них.

# Входные данные
# Первая строка входного файла INPUT.TXT содержит натуральное число N (N ≤ 100) – количество учеников (не считая Петю). 
# Во второй строке записаны N натуральных чисел Ai (Ai ≤ 200) – рост учеников в сантиметрах в порядке невозрастания. 
# Третья строка содержит единственное натуральное число X (X ≤ 200) – рост Пети.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите единственное целое число – номер Пети в шеренге учеников.
import random

n = int(input('Введите число участников шеренги: '))

x = random.randint(145, 200)
growth = sorted([random.randint(145, 200) for i in range(n)], reverse=True)
print('Рост Пети: ',x)
result = []
if x in growth:
    index_x = growth.index(x)
    growth.insert(index_x, x)
    print(growth)
    print('Место Пети: ',index_x + 1)
else:
    if x not in growth:
        growth.append(x)
        result = sorted(growth, reverse=True)
        print(result)
        print('Место Пети: ', result.index(x)+1)