import io
my_f=io.open(r'E:\СПЕЦИАЛИСТ\GEEKBRAINS\Textovie_fales\Zadacha3_5.txt', encoding='utf-8')
my_list = my_f.read().split('\n')
print(my_list)
sotrudnic=[]
oklad=[]
for i in my_list:
        i = i.split()
        if int(i[2]) < 20000:
           sotrudnic.append(i[0])
        oklad.append(i[2])
print(f'Оклад меньше 20.000 у {sotrudnic}, средний оклад {round(sum(map(int, oklad)) / len(oklad),2)}')
