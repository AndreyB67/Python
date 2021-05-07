import random

def shortBubbleSort(array):
    exchanges = True
    passnum = len(array)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if array[i]<array[i+1]:
                exchanges = True
                array[i], array[i + 1] = array[i + 1], array[i]
    passnum = passnum+1

array = [random.randint(0, 100) for _ in range(10)]
print(f'Исходный массив: {array}')
shortBubbleSort(array)
print(f'Сортированный массив: {array}')
