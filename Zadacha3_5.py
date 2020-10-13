def Strochka_cifr():
    res = 0
    while True:
        numbers = input('Введите список цифр или * для выхода: ').split()
        for i in numbers:
            try:
                if i == '*':
                    print('Exit')
                    return res
                else:
                    res += int(i)
            except ValueError:
                print('Введите цифру или *')
        print(res)
print (Strochka_cifr())

