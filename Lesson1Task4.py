def CodeDec(text):
    text=str(text)
    bytes_encoded = text.encode(encoding='utf-8')
    str_decoded = bytes_encoded.decode()
    print(bytes_encoded)
    print(str_decoded)


print('============================')

var = ['класс', 'администрирование', 'protocol', 'standard']
for i in var:
    a = i.encode('utf-8')
    print(a, type(a))
    b = bytes.decode(a, 'utf-8')
    print(b, type(b))


