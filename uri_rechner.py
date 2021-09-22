u2 = "V"
r2 ="Ohm"
i2 ="A"
again2 = ""
while again2 != 2:
    if again2 == 2:
        break                  
    operator=""
    operator = input("Geben sie (U) für Spannung , (R) für Wiederstand , (I) für Stromstärke oder (E) für EXIT ein : ")
    operator = operator.lower()
    if operator == "u":
        r=float(input("Geben sie den Wiederstand in Ohm an :"))
        i=float (input("Geben sie die Stromstärke in Ampere an :"))
        u1 = r*i
        print("Die Formel Lautet u = r*i ")
        print("Die Lösung ist  : " , u1,u2)
    if operator == "r":
        u=float(input("Geben sie die Spannung in Volt an : "))
        i=float(input("Geben sie den Strom in Ampere an :"))
        r1 = u/i
        print("Die Formel Lautet r = u/i ")
        print("Die Lösung ist  : " , r1,r2)
    if  operator =="i":
        u=float(input("Geben sie die Spannung in Volt an : "))
        r=float(input("Geben sie den Wiederstand in Ohm an :"))
        i1=u/r
        print("Die Formel Lautet i=u/r ")
        print("Die Lösung ist : " , i1,i2)
    if operator =="e":
        break
    again2 =int(input("Noch eine ? Yes(1)/No(2) : "))
print("Auf Wiedersehen ! ")   