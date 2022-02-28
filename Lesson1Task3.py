text_1='attribute'
text_2='класс'
text_3='функция'

TEXT=[text_1,text_2,text_3]

def ByteImposible(line):
    for item in line:
        try:
            uni_line=eval(f"b'{item}'")
        except SyntaxError:
            print('Recode',item,' imposible')

print(ByteImposible(TEXT))




