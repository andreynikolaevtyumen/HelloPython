# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите 
# на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

import os
os.system('cls')

def is_int(number):
    return number.isdigit()

number = None
while not is_int(str(number)):
    number = input('Введите число: ')

number = int(number)

result = dict()
for i in range(1, number + 1):
    result[i] = round((1 + 1/i)**i)

my_sum = 0
for i in result:
    my_sum += result[i]

print(result, '->', my_sum)