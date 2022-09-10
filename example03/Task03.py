# 3.Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
# Входные данные
# Входной файл INPUT.TXT содержит целое число N (1 < N ≤ 106).

# Выходные данные
# В выходной файл OUTPUT.TXT выведите ответ на задачу.



from re import I


numbers = int(input('Введите число: '))
print(numbers)

lst = [i for i in range(2, numbers + 1) if numbers % i == 0] # поиск делителей. 

#print(min(lst)) # решение через функцию min
print(lst) # сам список.

devider = lst[0] if lst else None # если список пустой

for i in lst: # поиск наименьшего делителя.
    if i < devider:
        devider = i
print("самый маленький делитель: ", devider)
