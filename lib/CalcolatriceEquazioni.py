from tkinter import *
import math

def calcola():
	p1 = e1.get()
	p2 = e2.get()
	

def pulisci():
	e1.delete(0, END)
	e2.delete(0, END)
	o1.configure(text="")

window = Tk()
window.title("Equazioni")
icon = PhotoImage(file='icon1.png')
window.tk.call('wm', 'iconphoto', window._w, icon)
window.geometry("550x200")

input = Label()
input.pack()

t1 = Label(input,text="Inserisci l'equazione:", width=20)
t1.grid(column=0, row=0)

e1 = Entry(input, width=19)
e1.grid(column=1, row=0)

t2 = Label(input, text="=", width=2)
t2.grid(column=2, row=0)

e2 = Entry(input, width=19)
e2.grid(column=3, row=0)

bottoni = Label()
bottoni.pack()

b1 = Button(bottoni, text="Risolvi", width=10, command=calcola)
b1.grid(column=0, row=1)

b1 = Button(bottoni, text="Pulisci", width=10, command=pulisci)
b1.grid(column=1, row=1)

b1 = Button(bottoni, text="Esci", width=10, command=quit)
b1.grid(column=2, row=1)

output = Label()
output.pack()

o1 = Label(output, width=40, bg="orange")
o1.grid(column=0, row=0)

window.mainloop()