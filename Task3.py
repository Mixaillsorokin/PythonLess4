# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

import random
Spisok1=[1,8,2,3,2,8,1,5,6]
Spisok2=[]
print(f'Исходный список : {Spisok1}')
for i in Spisok1:
    if not i in Spisok2:
        Spisok2.append(i)

print(f'Отфильтрованный список : {Spisok2}')
