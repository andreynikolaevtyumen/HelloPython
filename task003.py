# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится 
# эта точка (или на какой оси она находится). 
# Пример: - x=34; y=-30 -> 4 - x=2; y=4-> 1 - x=-34; y=-30 -> 3

import os
os.system('cls')

x = float(input('Введите коордирату X (не равную 0): '))
y = float(input('Введите коордирату Y (не равную 0): ')) 

if x>0 and y>0:
    print('Точка находится в I четверти плоскости')
elif x<0 and y>0:
    print('Точка находится в II четверти плоскости')
elif x>0 and y>0:
    print('Точка находится в III четверти плоскости')
elif x<0 and y<0:
    print('Точка находится в IV четверти плоскости')
elif x == 0 or y == 0:
    print('Внимание! Координаты X и Y не должны быть равны 0. Введите координаты еще раз.')