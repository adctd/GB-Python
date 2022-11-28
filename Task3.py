# Напишите программу, которая на вход принимает 5 чисел
# и находит максимальное из них

max = int(input())
for i in range(4):
    b = int(input())
    if b > max:
        max = b
print(max)

# a = list(map(int, input().split()))
# print(max(a))
