# Тесты выполнены на 64-разрядной Win 10
# Python 3.9.1 ([MSC v.1927 64 bit (AMD64)] on win32


import sys

#воспользуеся функцией для подсчета затрат
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

print('Введите трехзначное целое число')
a = int(input('Введите число '))
b = a//100
c = (a//10) % 10
d = a % 10


print('Сумма чисел',b+c+d)
print('Произведение чисел',b*c*d)

#
print('Переменные занимают',memory_count({b})+memory_count({a})+memory_count({c})+memory_count({d}))
sum_size = 0
sum_size += sys.getsizeof(a)
sum_size += sys.getsizeof(c)
sum_size += sys.getsizeof(d)
sum_size += sys.getsizeof(b)

print('Переменные занимают', sum_size)

#выведем свод затрат памяти
for i in dir():
    print(i, sys.getsizeof(i))

#Переменные занимают 112
#Дополнительная затрата памяти 258
#Итого 370







