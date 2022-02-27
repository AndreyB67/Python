from chardet import detect

f = open("test_file",'w',encoding='utf8')
f.write('сетевое программирование сокет декоратор')
f.close()

#+++++++++++++++++++++++++++++++++++++++++
with open("test_file",'rb') as f:
    conten=f.read()
encoding=detect(conten)['encoding']
print('encoding is:  ',encoding)

with open('test_file', 'r', encoding=encoding) as f_n:
    for i in f_n:
        print(i)


