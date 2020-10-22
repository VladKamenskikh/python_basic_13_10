"""
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def division():
    """
    Функция принимает два позиционных аргумента и выполняет их деление.
    """
    while True:
        try:
            numerator = int(input("Enter numerator: "))
            denominator = int(input("Enter denominator: "))
            break
        except ValueError:
            print("You can do better!")
    if denominator != 0:
         return numerator / denominator
    else:
        print("You cannot divide to zero!")


print(f'Result: {division():.0f}')
