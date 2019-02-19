"""Фильм «Пятница»,
сеансы: 12 часов – 250 руб, 16 – 350 руб, 20 – 450 руб.
Фильм «Чемпионы»,
сеансы: 10 часов – 250 руб, 13 – 350 руб, 16 – 350 руб.
Фильм «Пернатая банда»,
сеансы: 10 часов – 350 руб, 14 – 450 руб, 18 – 450 руб. """
film = input('Выбрать фильм: ')
date = input('Выбрать дату (сегодня, завтра): ')
time = int(input('Выбрать время: '))
tickets = int(input('Указать количество билетов: '))
def number_of_people(n):
    global m
    m = 0
    if n >= 20:
        m = 0.2
        print('Ваша скидка составит 20% ')
def discount(n):
    global l
    l = 0
    if n == 'завтра':
        l = 0.05
        print('Ваша скидка составит 5% ')
    elif n == 'сегодня':
        print('К сожалению, у вас нет скидки ')
    else:
        print('Вы ввели неверную дату')
def friday(n):
    global p
    if n == 12:
        p = 250
    elif n == 16:
        p = 350
    elif n == 20:
        p = 450
def champions(n):
    global p
    if n == 10:
        p = 250
    elif n == 13:
        p = 350
    elif n == 16:
        p = 350
def gang(n):
    global p
    if n == 10:
        p = 350
    elif n == 14:
        p = 450
    elif n == 18:
        p = 450
def cinema_price(n):
    global price
    if n == 'Пятница':
        friday(time)
        discount(date)
        number_of_people(tickets)
        price = tickets * (p-(p * l)-(p * m))
        print('Итого к оплате: ', price)
    elif n == 'Чемпионы':
        champions(time)
        discount(date)
        number_of_people(tickets)
        price = tickets * (p-(p * l)-(p * m))
        print('Итого к оплате: ', price)
    elif n == 'Пернатая банда':
        gang(time)
        discount(date)
        number_of_people(tickets)
        price = tickets * (p-(p * l)-(p * m))
        print('Итого к оплате: ', price)
    else:
        print('Такого фильма нет')
cinema_price(film)
