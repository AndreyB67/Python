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

summa = (a // 100) + ((a // 10) % 10) + (a % 10)
mult = (a // 100) * ((a // 10) % 10) * (a % 10)

print(f'Сумма цифр в числе: {summa}')
print(f'Произведение цифр в числе: {mult}')


sum_size = 0
sum_size += sys.getsizeof(a)
sum_size += sys.getsizeof(summa)
sum_size += sys.getsizeof(mult)
print('Переменные занимают', sum_size)


#выведем свод затрат памяти
for i in dir():
    print(i, sys.getsizeof(i))

#Переменные занимают 84
#Дополнительная затрата памяти 232
#Итого 316



