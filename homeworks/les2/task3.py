"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна,
лето, осень). Напишите решения через list и через dict.
"""
month = {}
month['1'] = 'January'
month['2'] = 'February'
month['3'] = 'March'
month['4'] = 'April'
month['5'] = 'May'
month['6'] = 'June'
month['7'] = 'July'
month['8'] = 'August'
month['9'] = 'September'
month['10'] = 'October'
month['11'] = 'November'
month['12'] = 'December'

Winter = ['December', 'January', 'February']
Spring = ['March', 'April', 'May']
Summer = ['June', 'July', 'August']
Fall = ['September', 'October', 'November']

input = month.get(input('Enter number from 1 to 12: '))
if input in Winter:
    print("It's Winter time!")
elif input in Spring:
    print("It's Spring time!")
elif input in Summer:
    print("It's Summer time!")
else:
    print("It's Fall time!")