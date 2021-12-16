alphabet = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "a":10, "b":11, "c":12, "d":13, "e":14, "f":15, "g":16, "h":17, "i":18, "j":19, "k":20, "l":21, "m":22, "n":23, "o":24, "p":25, "q":26, "r":27, "s":28, "t":29, "u":30, "v":31, "w":32, "x":33, "y":34, "z":35}

run = True

def get(alphabet):
    e = False
    
    try:
        s1 = int(input("From number system?: "))
        if s1 > 36:
            e = "Maximum is 36 (in \"From number system?: \")"
            
        elif s1 < 2:
            e = "Minimum is 2 (in \"From number system?: \")"
        
    except ValueError:
        e = "You are not allowed to type text here, only numbers (in \"From number system?: \")"
        s1 = 10000
        
    try:
        s2 = int(input("To number system?: "))
        if s2 > 36:
            e = "Maximum is 36 (in \"To number system?: \")"
            
        elif s2 < 2:
            e = "Minimum is 2 (in \"To number system?: \")"
        
    except ValueError:
        e = "You are not allowed to type text here, only numbers (in \"To number system?: \")"
    
    c1 = input("Number?: ").lower()
    for i in c1:
        if not alphabet[i] < s1:
            e = "None of digits in \"number\" can be biger than First number system (in \"Number?: \")"
    
    return s1, s2, c1, e

def flip(text):
    a = ""
    for i in text: a = i + a
    return a

def na(cislo, na):
    c1 = cislo
    for i in range(na-1): c1 *= cislo
    return c1

def to_decimal(cislo, alphabet, s1):
    cislo = flip(cislo)
    nasobek = 1
    c1 = 0
    bit = 0
    for i in cislo:
        bit += 1
        c1 += alphabet[i] * nasobek
        nasobek = na(s1, bit)
        
    return c1

def to_s(cislo, alphabet, s2):
    pass

while run:
    s1, s2, c1, e = get(alphabet)
    if not e == False:
        print(f"\nThere is an issue with what you have passed \nSee the problem here:\n{e}\n")
        
        
    else:
        if s2 == 10:
            print(to_decimal(c1, alphabet, s1), "\n")

        else:
            print(to_s(to_decimal(c1, alphabet, s1), alphabet, s2), "\n")

