import random
import statistics

def rt(array):
    left=[]
    right=[]
    middle=sum(array)/len(array)
    print(middle)
    print(len(array)//2)
    while len(left)<len(array)//2 and len(right)<=len(array)//2:
        for i in array:
            if i < middle:
                left.append(i)
            else:
                right.append(i)
        next
    return min(right)


def median(array):
    half = len(array) // 2
    array.sort()
    if not len(array) % 2:
        return (array[half - 1] + array[half]) / 2
    return array[half]


n = int(input('Введите натуральное число'))
array = [random.randint(0, 100) for _ in range(2 * n + 1)]

print(f'Исходный массив {array}')

print(f'Медиана массива ', rt(array))

print(f'Медиана массива статисика', statistics.median(array))

print(f'Медиана массива median', median(array))