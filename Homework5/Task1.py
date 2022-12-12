# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 117 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

from random import randint

def input_data(name):
    x = int(input(f"{name}, сколько конфет возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def message(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # очередность
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_data(player1)
        counter1 += k
        value -= k
        flag = False
        message(player1, k, counter1, value)
    else:
        k = input_data(player2)
        counter2 += k
        value -= k
        flag = True
        message(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")