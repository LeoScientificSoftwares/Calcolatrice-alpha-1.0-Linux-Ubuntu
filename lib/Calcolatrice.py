from tkinter import *

window = Tk()
window.title("Calcolatore")
icon = PhotoImage(file='icon1.png')
window.tk.call('wm', 'iconphoto', window._w, icon)
window.geometry("600x210")

def calcola():
	x = float(e1.get())
	y = float(e3.get())
	z = e2.get()
	if z=="+":
		a = x+y
		t4.configure(text=a)
	elif z=="-":
		a = x-y
		t4.configure(text=a)
	elif z=="x":
		a = x*y
		t4.configure(text=a)
	elif z==":":
		a = x/y
		t4.configure(text=a)
	else:
		return x

def pulisci():
	e1.delete(0, END)
	e2.delete(0, END)
	e3.delete(0, END)
	t4.configure(text="")

t1 = Label(text="Inserisci un numero", width=20)
t1.grid(column=0, row=0)

e1 = Entry(width=20)
e1.grid(column=1, row=0)

t2 = Label(text="Inserisci l'operatore", width=20)
t2.grid(column=0, row=1)

e2 = Entry(width=20)
e2.grid(column=1, row=1)

t3 = Label(text="Inserisci un numero", width=20)
t3.grid(column=0, row=2)

e3 = Entry(width=20)
e3.grid(column=1, row=2)

b1 = Button(text="Calcola", command=calcola, width=20)
b1.grid(column=0, row=3)

b1 = Button(text="Pulisci", command=pulisci, width=20)
b1.grid(column=1, row=3)

b1 = Button(text="Esci", command=quit, width=20)
b1.grid(column=2, row=3)

t4 = Label(height=5, width=20, bg="orange")
t4.grid(column=1, row=4, pady=5)

t5 = Label(width=20, text="Risultato")
t5.grid(column=0, row=4, pady=5)

window.mainloop()