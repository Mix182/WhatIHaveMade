def odmocnina(a, b):
    try:
        c = a ** (1 / b)
    except Exception:
        c = 1
    return c

def posloupnost(a):
    b = []
    for i in range(a - 1):
        b.append(i + 2)

    return b

def je_prvocislo(a):
    b = True
    for i in range(int(odmocnina(a, 2) + 1) - 2):
        i = i + 2
        if a % i == 0:
            b = False

    return b

def dostat_prvocisla(a):
    b = []
    for i in range(a):
        if je_prvocislo(a-i):
            b.append(a-i)

    b.remove(1)

    return b

def prvociselny_rozklad(a):
    b = []
    while not a == 1:
        c = dostat_prvocisla(a)
        for i in c:
            if a % i == 0:
                b.append(i)
                a = a // i

    return b

if __name__ == "__main__":
    run = True
    while run:
        a = input("Zadejte čislo:\n")
        if a == "q":
            quit()

        try:
            a = int(a)
            if a <= 0:
                print("Tohle je záporné číšlo, prosím zkuste to znovu!")
                continue
        
        except ValueError:
            print("tohle není číslo, prosím zkuste to znovu!")
            continue

        b = []
        for i in posloupnost(a):
            c = prvociselny_rozklad(i)
            for j in c:
                if not b.count(j) >= c.count(j):
                    for k in range(c.count(j) - b.count(j)):
                        b.append(j)
        d = 1
        for i in b:
            d *= i

        print(f"Nejmenší možné číslo, které je dělitelné čísly od 1 do {a} beze zbytku, je: {d}")
