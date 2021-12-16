import turtle

pen = turtle.Turtle()
pen.pendown()
pen.pensize(5)

def op():
    print("rozkaz")
    q = 0
    button = 1
    f = 0
    while f == 0:
        button = input( )
        
        if button == "w":
            pen.forward(50)

        elif button == "s":
            pen.back(50)

        elif button == "a":
            pen.left(90)

        elif button == "d":
            pen.right(90)

        elif button == "q":
            q += 1
            
            if q == 2:
                q = 0
            
            if q == 1:
                pen.penup()

            elif q == 0:
                pen.pendown()

            else:
                print(" ")

        elif button == "e":
            pen.clear()

        elif button == "f":
            f = 1

        else:
            print(" ")

    f = 0
            

def srdce():
    r = input("zadejte velikost ")
    r = int( r )
    r2 = r / 2
    r2 = int(r2)
    
    print("pracuji na tom")
    pen.right(45)
    pen.left(90)
    pen.forward( r )
    pen.left(90)
    pen.forward( r2 )
    pen.left(90)
    pen.forward( r2 )
    pen.right(90)
    pen.forward( r2 )
    pen.left(90)
    pen.forward( r2 )
    pen.left(90)
    pen.forward( r )
    print("hotovo!")
    pen.left(45)

def čtverec():
    a = 1
    r = input("velikost strany ")
    r = float(r)
    print("pracuji na tom")
    
    while a < 5:
        a += 1
        pen.forward( r )
        pen.right(90)
    print("hotovo!")
    


def kružnice():
    a = 1
    r = input("velikost kružnice ")
    r = float(r)
    print("pracuji na tom")
    
    while a < 361:
        a += 1
        pen.forward( r )
        pen.right(1)
    print("hotovo")

def trojúhelník():
    a = 1
    r = input("velikost strany ")
    r =  float(r)
    print("pracuji na tom")

    while a < 4:
        a += 1
        pen.forward( r )
        pen.left(120)
    print("hotovo!")
    
while True:

    color = input("Jaká barva? ")

    if color == "červená":
        pen.color("red")
        
    elif color == "modrá":
        pen.color("blue")

    elif color == "zelená":
        pen.color("green")

    elif color == "žlutá":
        pen.color("yelow")

    elif color == "černá":
        pen.color("black")

    elif color == "světle modrá":
        pen.color("cyan")

    elif color == "fialová":
        pen.color("purple")

    elif color == "/op @s":
        op()
        
    else:
        print("Tato barva zatím nebyla přidána !!!")

    shape = input("Co chcete nakreslit? (srdce, čtverec, kružnice, trojuhelník) ")

    pen.pendown()

    if shape == "srdce":
        srdce()
            
    elif shape == "čtverec":
        čtverec()

    elif shape == "kružnice":
        kružnice()

    elif shape == "trojúhelník":
        trojúhelník()
        
    else:
        print("tento tvar neznám !!!")

    an = input("chcete to smazat? ")
    
    if an == "ano":
        pen.clear()
        print("rozkaz")
        
    else:
        print("ok")
