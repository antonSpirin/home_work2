# Угадай год и дату рождения А.С. Пушкина (while & if)
year_of_birth = 0
day_birth = 0
month_birth = 0
while year_of_birth != 1799:
    year_of_birth = int(input('Введите год рождения А.С.Пушкина - '))
    if year_of_birth != 1799:
        print('Вы ввели не верный год рождения, попробуйте снова')
    elif year_of_birth == 1799:
        while day_birth != 6 or month_birth != 6:
            day_birth = int(input('Введите день рождения -'))
            month_birth = int(input('Введите месяц рождения - '))
            if day_birth != 6 or month_birth != 6:
                print('Вы ввели не верную дату рождения, попробуйте ещё раз')

print('Поздравляем! Вы ввели верный год и дату рождения А.С. Пушкина')
