my_list = [6,8,111,25,657,55,59,111,32,25,11,55]
my_new_list = [i for i in my_list if my_list.count(i) < 2]
print(my_new_list)