elem = input("Введите атомный номер: ")
if elem:
    nu = int(elem)
    if nu == 3:
        print("Это литий")
    elif nu == 25:
        print("Это марганец")
    elif nu == 80:
        print("Это ртуть")
    elif nu == 17:
        print("Это хлор")
    else:
        print("Что это??")
else:
    print("Введите значение атомный номер!")
