'''
 Напишите программу, доказывающую или 
 проверяющую, что для множества 
 натуральных чисел выполняется 
 равенство: 1+2+...+n = n(n+1)/2, 
 где n - любое натуральное число
'''

def storona1(n):
    if n == 1:
        return n
    elif n > 0:
        return n + storona1(n-1)

def storona2(n):
    return n * (n + 1) // 2

n = 1

while True and n < 997:
    if storona1(n) == storona2(n):
        print(f'Для n={n} - True')
    else:
        print(f'Для n={n} - False')
        break
    n += 1