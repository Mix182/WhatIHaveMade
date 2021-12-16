def root(a, b):
    try:
        c = a ** (1 / b)
    except Exception:
        c = 1
    return c

def continuity(a):
    b = []
    for i in range(a - 1):
        b.append(i + 2)

    return b

def is_prime(a):
    b = True
    for i in range(int(root(a, 2) + 1) - 2):
        i = i + 2
        if a % i == 0:
            b = False

    return b

def get_primes(a):
    b = []
    for i in range(a):
        if is_prime(a-i):
            b.append(a-i)

    b.remove(1)

    return b

def prime_decomposition(a):
    b = []
    while not a == 1:
        c = get_primes(a)
        for i in c:
            if a % i == 0:
                b.append(i)
                a = a // i

    return b


run = True
while run:
    a = input("enter number:\n")
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
    for i in continuity(a):
        c = prime_decomposition(i)
        for j in c:
            if not b.count(j) >= c.count(j):
                for k in range(c.count(j) - b.count(j)):
                    b.append(j)
    d = 1
    for i in b:
        d *= i

    print(f"Nejmenší možné číslo, které je dělitelné čísly od 1 do {a} beze zbytku, je: {d}")
