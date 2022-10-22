# 1.	Вычислить число c заданной точностью d
# Пример:
#       - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# В алгоритме использована серия Нилаканта: Пи = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10)...

from math import pi
from decimal import *

def nilakant(iteration):                       
        result = Decimal(3.0)
        factor = 1
        n = 2
        for n in range(2 ,2*iteration+1 ,2):
                result += 4/Decimal(n*(n+1)*(n+2)*factor)
                factor *= - 1
        return result
    
d = int(input('Задайте точность числа Пи d = '))
iteration = int(input('Введите количество повторений, для обеспечения полного совпадения:  '))
print(f'Полученное значение числа  Пи = {round(nilakant(iteration), d)}')
print(f"Контрольное значение числа Пи = {round((pi), d)}")