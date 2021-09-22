#Variablen

Auswahl=""

# Eingabe des Benutzers
print ("Hello, World!")
name = input("Enter your name: ")
print("Hello" ,name)
print(" ")
# Was wollen Sie Tun ?

while Auswahl != 6:
    print("Was wollen Sie tun? ")
    Auswahl = int (input ("Taschenrechner(1) URI-Rechner(2) Datum&Uhrzeit(3) Ratespiel(4) Wärungsrechner(5) Exit(6): " ))

    #Taschenrechner Funktion
    if Auswahl == 1:
        again =""
        ask=True 
        while again != 2:            
            if again == 2:
                break 
        # Eingabe der Variablen 
            while ask :
                c =  int (input ("Addieren? (1) , Subtrahieren? (2) , Multipliezieren? (3) , Dividieren? (4): "))
                if c>=5 :
                    print("ungültige Eingabe!")
                else:
                    a =  float (input ("Variable a:" ))  
                    b =  float (input ("Variable b:" ))
                    ask =False
            # Wahl des Rechen Operators 
            
            # Berechnung der Aufgabe
            if c == 1:
                d = a+b 
                print("The Answer is: " ,d)
            elif c == 2:
                d = a-b
                print("The Answer is: " ,d)
            elif c == 3:
                d = a*b
                print("The Answer is: " ,d)
            elif c == 4:
                if  b == 0 :
                    print("Teilen durch null nicht möglich!")
                else :
                    d = a/b
                    print("The Answer is: " ,d)
            ask=True
            again = int(input("Noch eine ? JA(1)/Nein(2): "))
    #URI Rechner
    if Auswahl == 2:
        u1= "V"
        r1="Ohm"
        i1="A"
        again2 = True
        while again2 :
            operator=0
            ask2=True
            while ask2 :
                operator = int(input("Geben sie (1) für Spannung , (2) für Wiederstand und (3) für Strom ein und (4) für exit : "))
                if operator ==4:
                    ask2 =False
                if operator >=5 :
                    print("ungültige Eingabe")
                else:
                    if operator == 1:
                        r=float(input("Geben sie den Wiederstand in Ohm an :"))
                        i=float (input("Geben sie die Stromstärke in Ampere an :"))
                        u = r*i
                        print("The Answer is : " , u,u1)
                    if operator == 2:
                        u=float(input("Geben sie die Spannung in Volt an : "))
                        i=float(input("Geben sie den Wiederstand in Ohm an :"))
                        if i == 0:
                            print("Teilen Durch 0 nicht möglich")
                        else: 
                            r = u/i
                            print("The Answer is :" , r,r1)
                    if  operator == 3:
                        u=float(input("Geben sie die Spannung in Volt an : "))
                        r=float(input("Geben sie den Wiederstand in Ohm an :"))
                        if r ==0:
                            print("Teilen durch 0 nicht möglich")
                        else:
                            i=u/r
                            print("The Answer is : " , i,i1)
        askagain =int(input("Wollen Sie das Programm beenden ? Yes(1)/No(2) : "))
        if askagain == 1:
            again2=False
        elif askagain == 2:
            again2 =True
    # Datum Uhrzeit
    if Auswahl == 3:
        import time
        lt = time.localtime()
        
        print("Es ist der {0:02d}.{1:02d}.{2:4d}".format (lt[2], lt[1], lt[0]))
        print("Uhrzeit: {0:02d}:{1:02d}:{2:02d}".format(lt[3], lt[4], lt[5]))

        wtage =["Mo", "Di","Mi","Do","Fr", "Sa", "So"]
        print("Wochentag:",wtage[lt[6]])

        print(time.strftime("KW,Beginn Montag: %W", lt))
    #Ratespiel
    if Auswahl == 4:
        again2=""
        game =int (input("Spielstarten? : Ja(1)/Nein(2) : "))
        while again2 != 2:            
            if again2 ==2:
                break                
            if game == 1 :                 
                import random
                n = 20
                to_be_guessed = random.randint(1,n)
                guess = 0        
                print("Gib eine Zahl von 1-20 ein bei 0 Spielabruch!") 
                while guess != to_be_guessed:
                    guess = int(input("Neuer Versuch: "))
                    if guess > 0:
                        if guess > to_be_guessed:
                            print("Zu gross")
                        if guess < to_be_guessed:
                            print("Zu klein")
                    if guess == 0:
                        print( name , "Schade, dass du aufgibst!")
                        break
                else:
                    print("Gratuliere, das war's")
                    again2 = int (input( "Nochmal ? Ja (1) / Nein (2): "))
            elif game == 2:
                    break
                    print ("Schade")
    #Forex & Krypto rechner
    if Auswahl == 5 :
        from forex_python.converter import CurrencyRates
        from forex_python.bitcoin import BtcConverter
        c = CurrencyRates()
        b = BtcConverter()
        start = ""
        while start != 2:
            start = int(input("Start (1), Exit (2)"))
            if start == 1:
                print("Der Aktuelle Euro Kurs ist: ")
                print(" ")
                print(c.get_rates('EUR'))
                print(" ")
                a = input("Von welcher Währung? ")  # von Welcher Währung 1, wird
                f = input("In zu welcher Währung? ")  # in Währung 2 umgerechnet
                d = float(input("Wie viel soll umgerechnet werden? " ))# Wie viel soll umgerechnet werden
                e = float(c.get_rate(a, f))
                g = e*d
                h = b.convert_to_btc(d, a)  # Wie viel soll in BTC umgerechnet werden
                j = "BTC"
                print("Die Antwort lautet:")
                print("Der Wechselkurs liegt bie:", '%.2f'%e, f)
                print("Der getauschte Betrag entspricht:", '%.2f'%g, f)
                print("In BTC sind das:", '%.8f'%h, j)
            if start == 2:
                break
    #exit programm
    if Auswahl >= 7 :
        print("unfültige eingabe")
print ("Auf Wiedersehen" , name + "!" )