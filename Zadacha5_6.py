import io
import re
subj = {}
with open(r'E:\СПЕЦИАЛИСТ\GEEKBRAINS\Textovie_fales\Zadacha5_6_2.txt', encoding='utf-8') as my_f:
    for line in my_f:
        try:
            subject, lecture, practice, lab = line.split()
        except ValueError:
            continue
        subj[subject] = sum(map(int,(re.findall('\d+', lecture) + re.findall('\d+',practice) + re.findall('\d+',lab))))
    print(f'Общее количество часов по предмету - \n {subj}')
