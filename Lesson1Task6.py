import locale

f = open("test_file.txt", "r")
print(f) # печатаем объект файла, что бы узнать его кодировку

file_coding = locale.getpreferredencoding()
print(file_coding)

# Читаем из файла
with open('resurs.txt', 'r', encoding=file_coding) as f_n:
    for i in f_n:
        print(i)

