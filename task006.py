# Напишите программу, которая принимает на вход вещественное число и показывает
# сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

import os
os.system('cls')

my_number = input('Введите вещественное число: ')

if float(my_number) < 0:                            
    my_number *= -1
figures_sum = 0

for i in str(my_number):
    if i != '.':
        figures_sum += int(i)

print(f'Сумма цифр введенного числа равна {figures_sum}')