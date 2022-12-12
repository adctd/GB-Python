# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# 6 -> [2,3]
# 144 -> [2,3]

from random import randint as rnd
def lists(a: int, uniq: bool = False) -> list[int]:
    i = 2
    lists = []
    while a != 1:
        while a % i == 0:
            lists.append(i)
            a //= i
        i +=1
    if uniq:
        return list(set(lists))
    else:
        return lists
a = rnd(10,9999)
print(f"Простые множители числа {a}: {lists(a)}")