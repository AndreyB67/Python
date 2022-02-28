text_1='class'
text_2='function'
text_3='method'

TEXT=[text_1,text_2,text_3]

def Infomation(line):
    for item in line:
        uni_line=eval(f"b'{item}'")
        print('тип переменной: {}\n'.format(type(uni_line)))
        print('содержание переменной - {}\n'.format(uni_line))
        print('длина строки:',len(uni_line))


print(Infomation(TEXT))



