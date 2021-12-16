while True:
    cislo = int(input("zadejte cislo \n"))
    c = cislo

    while c > 1:
        c -= 1
        cislo *= c
        
    print(cislo)
