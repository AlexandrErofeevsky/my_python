fir=input("Введите первое число")
oper=input("Введите операцию")
sec=input("Введите второе число")

def calc(a,b,c):
    try:
        a=int(fir)
        c=int(sec)
        if b=="+":
            return a+c
        elif b=="-":
            return a-c
        elif b=="*":
            return a*c
        elif b=="/":
            return a/c
    except ValueError:
        print("Введите числа!")
    except ZeroDivisionError:
        print("на 0 делить нельзя!")

print(calc(fir,oper,sec))
