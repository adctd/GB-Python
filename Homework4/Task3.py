# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint as rnd

lst = [rnd(1, 4) for i in range(12)]
print(f"Исходный список: {lst}")
print(f"Список из неповторяющихся элементов: {list(set(lst))}")