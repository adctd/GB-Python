# 3. Задайте два числа. Напишите программу, 
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Пример:
# 4, 5 -> 20
# 7,10 -> 70

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
def calculate_lcm(x, y):
    if x > y: 
        greater = x 
    else: 
        greater = y 
    while(True): 
        if((greater % x == 0) and (greater % y == 0)): 
            lcm = greater 
            break 
        greater += 1 
    return lcm
print(calculate_lcm(a,b))