import io
path = 'E:\СПЕЦИАЛИСТ\GEEKBRAINS\Textovie_fales\Zadacha2.txt'

with io.open(path, encoding='utf-8') as my_f:
    for line in my_f:
        print(line)
my_f=io.open(path, encoding='utf-8')
content = my_f.readlines()
print(content)
print(f'Количество строк в файле - {len(content)}')
my_f=io.open(path, encoding='utf-8')
content = my_f.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
my_f=io.open(path, encoding='utf-8')
content = my_f.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_f.close()

