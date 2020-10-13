def user(**kwargs):
    return list(kwargs.values())
Zaglavie = ['Имя', 'Фамилия', 'Год_рождения', 'Город_проживания', 'email', 'Телефон']
print(user(Имя=input('Enter name: '),
Фамилия=input('Enter second name: '),
Год_рождения=input('Enter birth day: '),
Город_проживания=input('Enter live town: '),
email=input('Enter email: '),
Телефон=input('Enter tel number: ')))







