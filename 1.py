def e1():
    x=input('Введите страну: ')
    stran={
        "Россия" : "Москва",
        "Италия" : "Рим",
        "Франция" : "Париж",
        "Финляндия" : "Хельсинки"
    }
    print("a", stran)
    print("b", stran[x])
    print("c", sorted(stran))

def e2():
    ochki={
        1 : ['А','а','в','е','н','о','р','с','т','В','Е','И','Н','О','Р','С','Т'],
        2 : ['д','к','л','м','п','у','Д','К','Л','М','П','У'],
        3 : ['Б','Г','Ё','Ь','Я','б','г','ё','ь','я'],
        4 : ['Й','Ы','',''],
        5 : ['Ж','З','Х','Ц','Ч','ж','з','х','ц','ч'],
        8 : ['Ш','Э','Ю','ю','ш','э'],
        10 : ['Ф','Щ','Ъ','ф','щ','ъ']
    }
    x = input("Введите слово")
    x=list(x)
    d=0
    for i in x:
        for k in ochki:
            if i in ochki[k]:
                d+=k
    print(d)

e2()
