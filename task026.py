# Напишите программу, которая принимает на вход число N и выдает набор произведений 
# чисел от 1 до N.

import os
os.system("cls")

from math import factorial

n = int(input('Введите число: '))
def list1(n):
    return [i for i in range(1,n+1)];
print(list1(n))
res = list(map(lambda x: factorial(x), list1(n))) # с помощью функции map и factorial 
# получаем результат
print(res)