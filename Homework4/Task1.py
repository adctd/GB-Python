# Вычислить число Пи c заданной точностью d
# *Пример:* 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415

import math
pi = math.pi
print('Pi =',pi)
d = 0.001
print(f'Accuracy = {d}')
count = 0
while d < 1:
    count += 1
    d = d*10
print('Pi =',round(pi, count))

from math import pi
def format_by_mask(num: float, accuracy: float) -> float:
    accuracy = str(accuracy)
    accuracy = len(accuracy[accuracy.find('.')+1::])
    return float(f'{pi:0.{accuracy}f}')

d = input('Введите точность в формате "0.01": ')
print(format_by_mask(pi, d))