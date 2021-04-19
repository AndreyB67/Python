"""
 Посчитать четные и нечетные цифры 
 введенного натурального числа. 
 Например, если введено число 34560, 
 то у него 3 четные цифры (4, 6 и 0) и 
 2 нечетные (3 и 5).
"""

a = input("Введите число: ")
chetnoe = 0
nechetnoe = 0
for i in a:
    if int(i)%2 == 0:
        chetnoe = chetnoe + 1
    else:
        nechetnoe = nechetnoe + 1
print('Четных цифр ',chetnoe)
print('Нечетных цифр ',nechetnoe)