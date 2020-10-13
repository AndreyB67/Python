def my_func(a, b, c):
    z = [a, b, c]
    z.remove(min(a, b, c))
    return sum(z)

a=int(input('Введите число '))
b=int(input('Введите число '))
c=int(input('Введите число '))
print (my_func(a, b, c))

