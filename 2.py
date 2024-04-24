def n1():
    a = (1, 2, 3, 4, 5)
    b = int(input("Введите чило: "))
    if b in a:
        print("Угадал")
    else:
        print("Не угадал")

def n2():
    d = []
    s = [1 ,3 ,5 ,3 ,5 ,2 ,6]
    for x in s:
        if s.count(x) > 1:
            if x not in d:
                d.append(x)
    print(*d)


def n3():
    days = ('Пн','Вт','Ср','Чт','Пт' ,'Сб','Вс')
    s = int(input('Введите количество выходных: '))
    for i in days:
        print('Рабочие дни: ', *days[:-s])
        print('Выходные дни: ', *days[-s:])
        break

def n4():
    import random
    gr1=('Абдурахимов','Дуничева','Клемешева','Синицина','Ломоносов','Жаркова','Вобла','Бутузова','Гирушев','Зарецкая')
    gr2=('Епифанов', 'Иванов','Окулова','Анисимов','Буланова','Кулакова','Доронин','Попова','Размахнина','Шарипов')
    a1=[]
    a2=[]
    a=[]
    a1.append(random.sample(gr1,5))
    a2.append(random.sample(gr2,5))
    a.extend(*a1)
    a.extend(*a2)
    a=tuple(a)
    print('a', *gr1)
    print('a', *gr2)
    print('a', *a)
    print('b', len(a))
    print('d', *sorted(a))
    print('e', 'Иванов' in a)
    print('e', a.count('Иванов)'))

n4()



