def Zaglavnaya1(text):
    ls1 = []
    #for i in range(len(text)):
    ls1.append(text[0].title() + text[1:])
    return ' '.join(ls1)


print(Zaglavnaya1(input('Input text: ')))

def ZaglavnayaAll(text):
    ls = []
    for i in range(len(text)):
        ls.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(ls)


print(ZaglavnayaAll(input('Input text: ').split(' ')))

