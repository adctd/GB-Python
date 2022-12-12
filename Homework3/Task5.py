# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.(Дополнительно)
# *Пример:*
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

k = int(input('Введите число: '))
negofibonacci = [1,-1]
fibonacci = [1,1]
for i in range(2,k):
    list = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(list)
    list_nego = negofibonacci[i-2] - negofibonacci[i-1]
    negofibonacci.append(list_nego)

negofibonacci.reverse()
negofibonacci.append(0)

print(f'для числа {k} => {negofibonacci+fibonacci}')

def fib(n):
    if n in [1, 2]:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)

def neg_fib(n: int) -> int:
    return (-1)**(n+1)*fib(n)

def sequence_of_fibs(n: int) -> list[int]:
    list1 = [neg_fib(i) for i in range(n+1)][::-1]
    list2 = [fib(i) for i in range(1, n+1)]
    return list1 + list2

n = 6
print(sequence_of_fibs(n))