"""
Реализовать функцию, принимающую несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон. Функция должна принимать параметры как именованные
аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def user_data():
    """
    Функция принимает данные пользователя и выводит одной строкой.
    """
    while True:
        try:
            name = input("Enter your name: ")
            surname = input("Enter your surname: ")
            date_of_birth = input("Enter your date of birth in format dd.mm.yy: ")
            town = input("Enter your town of residence: ")
            email = input("Enter your e-mail: ")
            phone_number = input("Enter your phone number: ")
            break
        except NameError:
            print("Try again")
        except ValueError:
            print("Try again")
    result = (f'Name: {name}; '
              f'Surname: {surname}; '
              f'Date of birth: {date_of_birth}; '
              f'Town: {town}; '
              f'E-mail: {email}; '
              f'Phone: {phone_number}')
    return result


print(user_data())
