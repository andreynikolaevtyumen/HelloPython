# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Пример:
# Входные данные: 'ываабв лповап абвцукв алоабвабв ываываыв'
# Выходные данные: 'лповап ываываыв'

import os
os.system('cls')

txt = input("Введите текст через пробел между словами:\n")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')