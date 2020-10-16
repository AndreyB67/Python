from sys import argv
vremya, zarplata, bonus = argv[1:]
try:
    vremya = float(input('Выработка в часах '))
    zarplata = int(input('Ставка в час руб. '))
    bonus = int(input('Премия в руб. '))
    viplata = vremya * zarplata + bonus
    print(f'Заработная плата сотрудника  {viplata}')
except ValueError:
    print('Not a number')
