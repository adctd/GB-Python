# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения 
# (D = b^2-4ac, x1 = (-b+/- sqtr(D))/a)
# 2) с помощью дополнительных библиотек Python(sympy, scipy)(Дополнительно)

from math import sqrt
a,b,c = list(map(int, input('Введите коэффициенты квадратного уравнения: ').split()))
d = b**2-4*a*c
if d>0:
    x1 = ((-b+sqrt(d))/(2*a))
    x2 = ((-b-sqrt(d))/(2*a))
    print(f'Два корня {x1} и {x2}')
elif d==0:
    x1 = (-b+sqrt(d)/(2*a))
    print(f'Корень один {x1}')
else:
    print(f'Действительных корней нет')

import sympy
x = sympy.Symbol('x')
a = input('Input eq:')
solutions = sympy.solve(a, x)
print(solutions)