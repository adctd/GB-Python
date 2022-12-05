# Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число. 
# ['ssss', 'sngujn556', 56] -> Yes ['56', 'sgnbsb'] -> No

list = ['ssss', 'sngujn556', 56]
count = 0
for i in list:
    if type(i) == int:
        print('есть число')
        count +=1
if count == 0:
    print('нет числа')
