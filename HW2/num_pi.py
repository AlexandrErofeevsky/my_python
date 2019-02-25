import math
n = int(input('Введите число: '))
p=math.pi
def number(n):
    return '{p:.{}f}'.format(n,p = math.pi)
print(number(n))
