import random

LenArray=50
array = [round(random.uniform(0, 49.99), 2) for i in range(LenArray)]
random.shuffle(array)

def merge_sort(array):

    if len(array) <= 1:
        return array

    left_side = merge_sort(array[:len(array) // 2])
    right_side = merge_sort(array[len(array) // 2:])

    i = j = 0
    result = []

    while i < len(left_side) or j < len(right_side):

        if i >= len(left_side):
            result.append(right_side[j])
            j += 1

        elif j >= len(right_side):
            result.append(left_side[i])
            i += 1

        elif left_side[i] < right_side[j]:
            result.append(left_side[i])
            i += 1

        else:
            result.append(right_side[j])
            j += 1

    return result


print(f'Исходный массив:{array}')
print(f'Сортированный массив:{merge_sort(array)}')