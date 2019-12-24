from tkinter import *
import math


def calcola():
    a1 = int(e1.get())
    a2 = int(e2.get())
    a3 = int(e3.get())
    a4 = int(e4.get())
    op = e5.get()
    if op == "+":
        c = a3 * a4
        y = a1 * a4
        z = a2 * a3
        b = y + z
        f = math.gcd(b, c)
        if f > 0:
            b = b / f
            c = c / f
        else:
            return b
        t4.configure(text=int(b))
        t6.configure(text=int(c))
    elif op == "-":
        c = a3 * a4
        y = a1 * a4
        z = a2 * a3
        b = y - z
        f = math.gcd(b, c)
        if f > 0:
            b = b / f
            c = c / f
        else:
            return b
        t4.configure(text=int(b))
        t6.configure(text=int(c))
    elif op == "x":
        b = a1 * a2
        c = a3 * a4
        f = math.gcd(b, c)
        if f > 0:
            b = b / f
            c = c / f
        else:
            return b
        t4.configure(text=int(b))
        t6.configure(text=int(c))
    elif op == ":":
        b = a1 * a4
        c = a2 * a3
        f = math.gcd(b, c)
        if f > 0:
            b = b / f
            c = c / f
        else:
            return b
        t4.configure(text=int(b))
        t6.configure(text=int(c))


def pulisci():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    t4.configure(text="")
    t6.configure(text="")


window = Tk()
window.title("Frazioni")
icon = PhotoImage(file='icon1.png')
window.tk.call('wm', 'iconphoto', window._w, icon)
window.geometry("325x200")

e1 = Entry(width=7)
e1.grid(column=0, row=0)

e2 = Entry(width=7)
e2.grid(column=2, row=0)

e3 = Entry(width=7)
e3.grid(column=0, row=2)

e4 = Entry(width=7)
e4.grid(column=2, row=2)

t1 = Label(text="----------------", width=7)
t1.grid(column=0, row=1)

t3 = Label(text="----------------", width=7)
t3.grid(column=2, row=1)

e5 = Entry(width=7)
e5.grid(column=1, row=1)

b1 = Button(text="Calcola", command=calcola, width=10)
b1.grid(column=0, row=3)

b2 = Button(text="Pulisci", command=pulisci, width=10)
b2.grid(column=1, row=3)

b3 = Button(text="Esci", command=quit, width=10)
b3.grid(column=2, row=3)

t4 = Label(width=7, bg="orange")
t4.grid(column=1, row=4)

t5 = Label(text="-----------------", width=7, bg="orange")
t5.grid(column=1, row=5)

t6 = Label(width=7, bg="orange")
t6.grid(column=1, row=6)

t7 = Label(width=7, text="Risultato:")
t7.grid(column=0, row=5)

window.mainloop()
