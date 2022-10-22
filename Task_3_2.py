# Задача 3.	Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst = list(map(int, input("Введите числа через пробел: ").split()))
lst2 = []
lst_result = []
for i in lst:
    if i in lst2:
        continue
    lst2.append(i) 
print(f'Исходный список: {lst} ')
print(f'Список с исключёнными повторами: {lst2}')

lst_replay_elem = [x for i, x in enumerate(lst) if i != lst.index(x)]
print(f'Список из повторяющихся элементов: {lst_replay_elem}')

for i in lst2:
    if i not in lst_replay_elem:
        lst_result.append(i)
 
print(f"Список из неповторяющихся элементов: {lst_result}")