# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

name = input('enter name: ')
lastname = input('enter lastname: ')
year = int(input('enter year: '))
city = input('enter city: ')
email = input('enter email: ')
telephone = input('input telephone:')

def my_func (name, lastname, year, city, email, telephone):
     return ' '.join([name, lastname, year, city, email, telephone])
print(my_func(lastname = 'Pavlov', name = 'Konstantin', year = '1992', city = 'Moscow', email = 'mail@mail.ru', telephone = '8-925-885-71-17'))