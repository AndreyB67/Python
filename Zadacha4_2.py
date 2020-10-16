my_list = [500, 7, 21, 66, 2, 13, 41, 210, 87, 151, 378, 1123, 515]
print(f'Исходный список {my_list}')
my_new_list = [j for i, j in zip(my_list, my_list[1:]) if j > i]
print(f'Новый список {my_new_list}')