print("Vítej v mé nejlípupravovatelnější hře")

jméno = input("Jaké je tvoje jméno? \n")
věk = input("Jaký je tvůj věk? \n")
věk = int(věk)

if věk >= 6:
    chce_hrát = input("Můžeš hrát ale, chceš vůbec? \n")
    
    if chce_hrát == "ano":
        tof = input("Dobře tak začneme. \nZe začátku máš 10 životů. \nVyber si: doprava \n          doleva \n")
        životy = int(10)
        Životy = str(životy)

        if tof == "doleva":
            životy -= 5
            Životy = str(životy)
            print("Zatím žiješ, ale máš jen" , Životy , "životů! (bodl jsi se o trn)")
            tof = input("Vyber si: \nChceš domů nebo přes řeku do Kauflandu? (domů, do Kauflandu)\n")

            if tof == "domů":
                print ("Jéj jsi doma kde máš lékárničku ta ti vyléčí 5 životů")
                životy += 5
                Životy = str(životy)

            else:
                tof = input("Řeka je plná krokodýlů, chceš hrát mrtvého nebo začít utíkat (hráz mrtvého, utíkat)\n")
                if tof == "utíkat":
                    print("Výborně krokodýlům jsi ůspěšně utekl")
                else:
                    print("krokodýli mají hlad a sežrali by i rok starou mršinu. \nHraním mrtvého jsi si nepomohl, byl jsi sežrán krokodýli.")
        else:
            print("Spadl jsi do propasti a umřel jsi!")

    else:
        print("Tak nic no.")

else:
    print("Promiň ale nemůžeš hrát, není ti ani šest!")
