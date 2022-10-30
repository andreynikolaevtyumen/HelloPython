# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.

import os
os.system("cls")

import random
list1 = [random.randint(1,10) for i in range(10)] # задаем список из 10 случайных чисел 
# от 1 до 10 
print(list1)
list1_odd = [list1[i] for i, list1[i] in enumerate(list1) if i%2!=0]
print(list1_odd)
print(sum(list1_odd)) # сумма нечетных позиций