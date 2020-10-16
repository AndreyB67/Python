from sys import argv

vremya, zarplata, bonus = argv[1:]
try:
    vremya = int(time)
    zarplata = int(zarplata)
    bonus = int(bonus)
    viplata = vremya * zarplata + bonus
    print(f'заработная плата сотрудника  {viplata}')
except ValueError:
    print('Not a number')