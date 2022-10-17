# Реализуйте алгоритм перемешивания списка.
import os
os.system('cls')

import random
lst = [random.randint(0, 10) for i in range(random.randint(5,20))]
print(f'Исходный список:\n {lst}')
random.shuffle(lst)
print(f'Перемещанный сеисок: \n{lst}')




# from time import time
# my_time = time()
# my_time %= 1
# print(int((my_time % 1)*100))
