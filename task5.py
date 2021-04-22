"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
"""


import random

r = [random.randint(-13, 13) for _ in range(13)]
print(f'Массив: {r}')

min_index = 0

for i in r:
    if r[min_index] > i:
        min_index = r.index(i)

if r[min_index] >= 0:
    print(f'В массиве лишь положительные элементы')
else:
    print(f'В массиве минимальный отрицательный элемент {r[min_index]} ',
            f'на позиции {min_index}')