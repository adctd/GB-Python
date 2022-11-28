print('hello world')

value = None
print(type(value))

a = 123
b = 1.23
value = 1234
print(value)

s = 'hello world'
print(s)

print(a, b, s)
print(a, '-' ,b, '-' ,s)
print('{} - {} - {}'.format(a, b, s))
print(f'{a} - {b} - {s}')

f = False
print(f)

list = []
print(list)

list = ['1', '2', '3', 'hello', 1,2,4.5,True]
print(list)

print('введите a')
a = input() #для целых чисел a = int(input())
print('введите b')
b = input() #для вещественных значений b = float(input())
print(a, b)
print('{} {}'.format(a, b))
print(f'{a} {b}')
print(a, ' + ', b, ' = ', a+b)

# Арифметические операции
# +, -, *, /, %, //, **
# Приоритет операций
# **, ⊕, ⊖, *, /, //, %, +, -
# ( ) Скобки меняют приоритет

a = 12
b = 8
c = a / b #будет 1.5, а если хотим целочисленное деление, то //
          #если хотим остаток, то %
          #если хотим возведение в степень то **
print(c)

a = 1.3123
b = 3
c = round(a * b, 5) #округление
print(c)

a = 3
a+=5 #присваивание (это означает a = a+5)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in
# gen

a = 1 < 4 and 5 > 2
print(a)

# Управляющие конструкции: if, if-else
# if condition:
 # operator 1
 # operator 2
 # ...
 # operator n
# else:                  ОТСТУПЫ ВАЖНЫ!
 # operator n + 1
 # operator n + 2
 # ...
 # operator n + m

username = input('Введите имя: ')
if username == 'Маша':
    print('Ура, это же МАША!')
elif username == 'Марина':
    print('Я так ждала Вас, Марина!')
elif username == 'Ильнар':
    print('Ильнар - топ)')
else:
    print('Привет, ', username)

# Управляющие конструкции: while
# while condition:
 # operator 1
 # operator 2                   ОТСТУПЫ ВАЖНЫ!
 # . . .
 # operator n

original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
 print('Пожалуй')
 print('хватит )')
print(inverted)

# Управляющие конструкции: for
# for i in enumeration:
 # operator 1
 # operator 2
 # . . .
 # operator n

for i in 1, -2, 3, 14, 5:
    print(i)

r = range(5) # range(0, 5)
r = range(2, 5) # range(2, 5)
r = range(-5, 0) # range(-5, 0)
r = range(1, 10, 2) # range(1, 10, 2)
r = range(100, 0, -20) # range(100, 0, -20)

text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #
for c in text:
    print(c)

text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
print(text[len(text)-1]) # к
print(text[-5]) # б
print(text[:]) # print(text)
print(text[:2]) # съ
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...

#СПИСКИ - это пронумерованная, изменяемая коллекция объектов

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2
 print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5]

#Функции - Это фрагмент программы, используемый многократно
def function_name(x):
    # body line 1
    # . . .
    # body line n
    # optional return

def f(x):
    return x**2

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType