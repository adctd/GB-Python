# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
print(list)
def dif(list):
    dif_max_min =[]
    for i in range(len(list)):
        dif_max_min.append(list[i]%1)
    return max(dif_max_min) - min(dif_max_min)
print(dif(list))

#def separate_fraction(num: float) -> float:
#    list_num = str(num).split('.')
#    return float('0.'+list_num[1])

#def max_vs_min_fraction(num_list: list[float]) -> float:
#    new_list = [separate_fraction(i) for i in num_list if int(i) != float(i)]
#    print(new_list)
#    return max(new_list) - min(new_list)

#example = [1.1, 1.2, 3.1, 5, 10.01]
#print(max_vs_min_fraction(example))