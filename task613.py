# Тесты выполнены на 64-разрядной Win 10
# Python 3.9.1 ([MSC v.1927 64 bit (AMD64)] on win32


import sys


def memory_count(lst):
    memory = 0

    for var in lst:
        print('***********')
        print(f'Переменная: {var}')
        print('Весит: ', sys.getsizeof(var))
        spam = sys.getsizeof(var)

        if hasattr(var, '__iter__') and not isinstance(var, str):

            if hasattr(var, 'keys'):
                for key, value in var.items():
                    print(f'\nКлюч: \'{key}\' значение {value}')
                    spam += memory_count([key]) + memory_count([value])

            else:
                spam += memory_count(var)

        memory += spam

    return memory


# Найти сумму и произведение цифр трехзначного числа,
# которое вводит пользователь.

# ***************************************************************************************************
a = int(input('Введите целое трехзначное число:'))

print(f'Сумма цифр в числе: {(a // 100) + ((a // 10) % 10) + (a % 10)}')
print(f'Произведение цифр в числе: {(a // 100) * ((a // 10) % 10) * (a % 10)}')

print(memory_count({a}))
# #
for i in dir():
    print (i, sys.getsizeof(eval(i)) )

sum_size = 0
sum_size += sys.getsizeof(a)

print('Переменные занимают', sum_size)

#выведем свод затрат памяти
for i in dir():
    print(i, sys.getsizeof(i))

#Переменные занимают 28
#Дополнительная затрата памяти 208
#Итого 236


# ВЫВОД: Использование значительного числа переменных занимает в памяти больше места, но они облегчают
# читабельность кода. Хорошим компромиссом является вариант 611.
