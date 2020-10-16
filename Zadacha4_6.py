from itertools import count

for item in count(int(input('Введите стартовое число '))):
    if item<10:
        print(item) # внимание - беконечный цикл!
    else:
        break

from itertools import cycle

my_list = ['Tom','Djon','Genry','Eliza',123, 'Dydya Sam']
count=0
for item in cycle(my_list):
    if count > 10:
        break
    print(item)
    count += 1