# 1.	Даны два файла, в каждом из которых находится запись многочлена. 
#       Задача - сформировать файл, содержащий сумму многочленов.



file_1 = 'Task_5_1.txt'
file_2 = 'Task_5_2.txt'
file_res = 'Task_5_resalt.txt'

poly_1 = (open(file_1, 'r')).read() # прочитали и сформировали строку
print(f'Строка первого многочлена: {poly_1}')

poly_1 = poly_1.replace('x^', ' ')  # отредактировали строку 
poly_1 = poly_1.replace(' +', '')
poly_2 = poly_1.replace(' -', '')
poly_1 = poly_1.replace('x', ' 1')

Lst_poly_1 = poly_1.split()              # сформировали список
print(f'Исходный список первого многочлена: {Lst_poly_1}')
Lst_poly_1_coeff = list(map(int, Lst_poly_1[:: 2]))
print(f'Список коэффицментов первого многочлена: {Lst_poly_1_coeff}')
Lst_poly_1_stepen = list(map(int, Lst_poly_1[1 : : 2]))
print(f'Список степеней первого многочлена: {Lst_poly_1_stepen}')

poly_1_dict = dict(zip(Lst_poly_1_stepen, Lst_poly_1_coeff))  # словарь, где в качестве ключа степень, а в качестве значения коэффициент
print(f'Словарь первого многочлена: {poly_1_dict}')
print()

poly_2 = (open(file_2, 'r')).read() # прочитали и сформировали строку
print(f'Строка второго многочлена: {poly_2}')

poly_2 = poly_2.replace('x^', ' ')  # отредактировали строку
poly_2 = poly_2.replace(' +', '')
poly_2 = poly_2.replace(' -', '')
poly_2 = poly_2.replace('x', ' 1')

Lst_poly_2 = poly_2.split()              # сформировали список
print(f'Исходный список второго многочлена: {Lst_poly_2}')
Lst_poly_2_coeff = list(map(int, Lst_poly_2[:: 2]))      # список коэффициентов
print(f'Список коэффициентов второго многочлена: {Lst_poly_2_coeff}')
Lst_poly_2_stepen = list(map(int, Lst_poly_2[1 : : 2]))  # список степеней 
print(f'Список степеней второго многочлена: {Lst_poly_2_stepen}')

poly_2_dict = dict(zip(Lst_poly_2_stepen, Lst_poly_2_coeff)) # словарь, где в качестве ключа степень, а в качестве значения коэффициент
print(f'Словарь второго многочлена: {poly_2_dict}')
print()

for key in poly_1_dict.keys():                                 # суммируем словари по соответствию ключей
     if key in poly_2_dict.keys():
        poly_1_dict[key] = poly_1_dict[key] + poly_2_dict[key]
        poly_sum_dict = poly_1_dict
poly_sum_dict[0]= Lst_poly_1_coeff[-1] + Lst_poly_2_coeff[-1]   # добавляем сумму коэффициентов при переменной со степенью '0' 

print(f'Сумма словарей многочленов: {poly_sum_dict}')

poly_sum_lst1 = list(poly_sum_dict.items()) # преобразовываем сумму словарей в список кортежей с парой степень - коэффициент
print(f'Список кортежей степень-коэффициент: {poly_sum_lst1}')

poly_sum_lst2 = [f'{(j,"")[j==1]}x^{i}' for i, j in poly_sum_lst1 if j]
print(f'Список, наполненный символами: {poly_sum_lst2}')

poly_sum =' + '.join(poly_sum_lst2)             # обратное преобразование списка в строку с заменой пробела на " + "
print(f'Обратное преобразование списка в строку: {poly_sum}')
print()

poly_sum = poly_sum.replace('x^1', 'x')
poly_sum = poly_sum.replace('x^0', '')
print(f'Cумма многочленов равна:  {poly_sum}')

with open(file_res, 'w') as text:
    text.write(poly_sum)