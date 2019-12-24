from subprocess import call
from tkinter import *

def calcnum():
	class callnum(object):

		def __init__(self, path="Calcolatrice.py"):
			self.path = path

		def call_calcnum(self):
			call(["python3", "{}".format(self.path)])

	if __name__ == "__main__":
		c = callnum()
		c.call_calcnum()

def calcfra():
	class callfra(object):

		def __init__(self, path="CalcolatriceFrazioni.py"):
			self.path = path

		def call_calcfra(self):
			call(["python3", "{}".format(self.path)])

	if __name__ == "__main__":
		c = callfra()
		c.call_calcfra()

def calcequ():
	class callequ(object):

		def __init__(self, path="CalcolatriceEquazioni.py"):
			self.path = path

		def call_calcequ(self):
			call(["python3", "{}".format(self.path)])

	if __name__ == "__main__":
		c = callequ()
		c.call_calcequ()

window = Tk()
window.title("Calcolatrice alpha 1.0")
icon = PhotoImage(file='icon1.png')
window.tk.call('wm', 'iconphoto', window._w, icon)
window.geometry("600x400")

a1 = Label()
a1.pack()

title = Label(a1, text="Calcolatrice", fg="Orange", font=("Courier", 40))
title.grid(column=0, row=0)

st = Label(a1,text="release alpha 1.0")
st.grid(column=0, row=1)

b1 = Label()
b1.pack()

bu1 = Button(b1, text="Calcolatrice Numerica", command=calcnum, width=17, height=5)
bu1.grid(column=0, row=0)

bu2 = Button(b1, text="Calcolatrice Frazioni", command=calcfra, width=17, height=5)
bu2.grid(column=1, row=0)


bu3 = Button(b1, text="Calcolatrice Equazioni \n (beta)", command=calcequ, width=17, height=5)
bu3.grid(column=2, row=0)

bu4 = Button(b1, text="Esci", command=quit, width=17, height=5)
bu4.grid(column=1, row=1)

window.mainloop()