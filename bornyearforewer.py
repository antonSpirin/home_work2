# Угадай год рождения А.С. Пушкина
year_of_birth = int(input('Введите год рождения А.С.Пушкина - '))

while year_of_birth != 1799:
    print('Вы ввели не верный год рождения, попробуйте снова')
    year_of_birth = int(input('Введите год рождения А.С.Пушкина - '))

print('Вы ввели верный год рождения')
