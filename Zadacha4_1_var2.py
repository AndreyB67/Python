vremy, salary, bonus = argv[1:]
try:
    vremy = int(vremy)
    zarplata = int(zarplata)
    bonus = int(bonus)
    res = vremy * zarplata + bonus
    print(f'заработная плата сотрудника  {res}')
except ValueError:
    print('Not a number')