import random
a = random.randint(1,4)
b=int(input('Введите число: '))
if a == b:
    print('Победа!!!')
else:
    print('Повторите ещё раз!')
    if a>b:
        print('Больше')
    else:
        print('Меньше')
