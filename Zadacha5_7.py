import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open(r'E:\СПЕЦИАЛИСТ\GEEKBRAINS\Textovie_fales\Zadacha5_7.txt', encoding='utf-8') as my_f:
    for line in my_f:
        print(line)
        name, firm, viruchka, izderjki = line.split()
        profit[name] = int(viruchka) - int(izderjki)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')
		  