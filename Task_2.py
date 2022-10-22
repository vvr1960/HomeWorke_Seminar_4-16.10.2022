# Задача 2.	Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


N = int(input("Введите натуральное число N: "))
i = 1 
lst_factors = []
lst_prime_factors = []

while i <= N:
    if N % i == 0:
        lst_factors.append(i)
        lst_prime_factors = list(set(lst_factors))
        N = N // i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {N} приведены в списке: {lst_prime_factors}")