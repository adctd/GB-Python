# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

N = int(input('Введите номер четверти: '))
if N == 1:
    print('Координаты будут в диапазоне х > 0, y > 0')
elif N == 2:
    print('Координаты будут в диапазоне х < 0, y > 0')
elif N == 3:
    print('Координаты будут в диапазоне х < 0, y < 0')
elif N == 4:
    print('Координаты будут в диапазоне х > 0, y < 0')

#Второй вариант решения через словарь
#a = input()
#d = {'1':'x>0 y>0', '2': 'x<0 y>0', '3': 'x<0 y<0', '4': 'x>0 y<0'}
#print(d[a])