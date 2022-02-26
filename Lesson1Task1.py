
def online_test(text):
    for item in text:
        print(item)
        print(type(item))

text_1=str('разработка')
text_2=str('сокет')
text_3=str('декоратор')

Text_String=[text_1,text_2,text_3]

print(online_test(Text_String))

#text1 to byte
unic_1=b'\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'

#text2 to byte
unic_2=b'\u0441\u043e\u043a\u0435\u0442'

#text3 to byte
unic_3=b'\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

Text_Unic=[unic_1,unic_2,unic_3]

print(online_test(Text_Unic))





