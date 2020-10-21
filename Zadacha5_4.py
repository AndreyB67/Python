perehodnic = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_f=[]
with open(r'E:\СПЕЦИАЛИСТ\GEEKBRAINS\Textovie_fales\Zadacha4_5.txt','r') as my_f:
    my_f = my_f.read().split('\n')
    for i in my_f:
        i = i.split(' ',1)
        new_f.append(perehodnic[i[0]] + ' ' + i[1]+' ')
print(new_f)

with open(r'E:\СПЕЦИАЛИСТ\GEEKBRAINS\Textovie_fales\Zadacha4_5_new.txt','w') as my_f_new:
    for element in new_f:
        print (element,file=my_f_new)
		