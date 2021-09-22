from tkinter import * 

Taschenrecher = Tk()
Taschenrecher.geometry ("400x350")
Taschenrecher.title("U-R-I Rechner")
i = IntVar() #Basically Links Any Radiobutton With The Variable=i.


Label(Taschenrecher, 
    text="""Willkommen im URI Rechner""",
    justify = LEFT,
    padx = 20).pack()

Label(Taschenrecher,text="Wählen Sie aus was sie Berechnen wollen",justify=LEFT ,padx= 40).pack()

auswahl = 0
entry1=""
entry2=""

def auswahl1 ():
    global auswahl, entry1, entry2
    auswahl=1
    labelstrom =Label(Taschenrecher,text="Geben Sie hier die Stromstärke ein :").place
    labelstrom.place(x=25 ,y=75, height= 25)
    labelwiederstand =Label(Taschenrecher,text="Geben Sie hier die Wiederstand ein :")
    labelwiederstand.place(x=25 ,y=125, height= 25)

    entry1 = Entry(master=Taschenrecher , bg="White")
    entry1.place(x=25 ,y=100, height=25)
    entry2 = Entry(master=Taschenrecher , bg="White")
    entry2.place(x=25 ,y=150, height=25)
def auswahl2 ():
    global auswahl, entry1, entry2
    auswahl=2
    labelspannung =Label(Taschenrecher,text="Geben Sie hier die Spannung ein :   ")
    labelspannung.place(x=25 ,y=75, height= 25)
    labelstrom =Label(Taschenrecher,text="Geben Sie hier die Stromstärke ein :")
    labelstrom.place(x=25 ,y=125, height= 25)

    entry1 = Entry(master=Taschenrecher , bg="White")
    entry1.place(x=25 ,y=100, height=25)
    entry2 = Entry(master=Taschenrecher , bg="White")
    entry2.place(x=25 ,y=150, height=25)
def auswahl3 ():
    global auswahl, entry1, entry2
    auswahl=3
    labelspannung =Label(Taschenrecher,text="Geben Sie hier die Spannung ein :   ")
    labelspannung.place(x=25 ,y=75, height= 25)
    labelwiederstand =Label(Taschenrecher,text="Geben Sie hier die Wiederstand ein :")
    labelwiederstand.place(x=25 ,y=125, height= 25)

    entry1 = Entry(master=Taschenrecher , bg="White")
    entry1.place(x=25 ,y=100, height=25)
    entry2 = Entry(master=Taschenrecher , bg="White")
    entry2.place(x=25 ,y=150, height=25)
def berechnen():
    global auswahl 
    if auswahl==1:
        i = float(entry1.get())
        r = float(entry2.get())
        u = i*r
        label_ergebnis.config(text=str(u))
    elif auswahl==2 :
        u=float(entry1.get())
        i=float(entry2.get())
        r=u/i
        label_ergebnis.config(text=str(r))
    elif auswahl==3:
        u = float(entry1.get())
        r = float(entry2.get())
        i = u/r
        label_ergebnis.config(text=str(i))
r1 = Radiobutton(Taschenrecher, text="Spannung (U)", value=1, variable=i, command= auswahl1).place(x=25,y=50 )
r2 = Radiobutton(Taschenrecher, text="Wiederstand (R)", value=3, variable=i, command=auswahl2).place(x=290,y=50 )
r3 = Radiobutton(Taschenrecher, text="Strom (I)", value=2, variable=i, command=auswahl3).place(x=170,y=50 )

# Button zum Berechnen
buttonBerechnen = Button(master=Taschenrecher, bg='#FBD975', text='Berechnen', command=berechnen )
buttonBerechnen.place(x=150, y=200, width=100, height=27)

label_ergebnis=Label(Taschenrecher,bg="lightgray", text="")
label_ergebnis.place(x=175 , y=250 , height=25 ,width=50)

Taschenrecher.mainloop()