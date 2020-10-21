from random import randint
numbers = []
for i in range(15):
    numbers.append(randint(0, 15))
    list=numbers
with open(r'E:\СПЕЦИАЛИСТ\GEEKBRAINS\Textovie_fales\Zadacha5_5.txt', 'r') as my_f:
    line = my_f.read()
    print(line)
    my_cifr = line.split()
    print(sum(map(int, my_cifr)))

