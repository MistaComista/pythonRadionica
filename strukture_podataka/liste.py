from tkinter import *
from tkinter import ttk
osobe=[]
def unesiLice(*args):
	try:
		tree.insert("" , 0,values=(nameVar.get(),surnameVar.get()))
		osobe.append((nameVar.get(),surnameVar.get()))
		nameVar.set("")
		surnameVar.set("")
		name.focus_set()
	except ValueError:
		pass
#imena na A
def calcul1():
	try:
		uneteReci=[elem[0] for elem in osobe if elem[0][0]=='A']
		osobeVar.set(" ".join(uneteReci))
	except:
		pass
def calculpo():
	try:
		uneteReci=[rec for elem in osobe for rec in elem]
		osobeVar.set(" ".join(uneteReci))
	except:
		pass
def calcul122():
	try:
		osobeVar.set("TO DO")
	except:
		pass
def calcul():
	try:
		imena=[y for x in osobe for y in x]
		osobeVar.set(" ".join(imena))
	except:
		pass
#uneteReci izdvaja samo imena
def calcul3():
	try:
		uneteReci=[elem[0] for elem in osobe]
		osobeVar.set(" ".join(uneteReci))
	except:
		pass
root = Tk()
nameVar = StringVar()
surnameVar = StringVar()
osobeVar=StringVar()
content = ttk.Frame(root)
namelbl = ttk.Label(content, text="Ime")
name = ttk.Entry(content,textvariable=nameVar)
surnamelbl = ttk.Label(content, text="Prezime")
surname = ttk.Entry(content,textvariable=surnameVar)
ok = ttk.Button(content, text="Unesi", command=unesiLice)
prikazi = ttk.Button(content, text="Prikazi", command=calcul)
osobelbl = ttk.Label(content, textvariable=osobeVar)
tree = ttk.Treeview(content)
tree['show'] = 'headings'
tree["columns"]=("prva","druga")
tree.heading("prva", text="Ime")
tree.heading("druga", text="Prezime")
content.grid(column=0, row=0, sticky=(N, S, E, W))
namelbl.grid(column=0, row=0, sticky=(N, W), padx=5)
name.grid(column=1, row=0,sticky=(N, W), padx=5)
surnamelbl.grid(column=2, row=0, sticky=(N, W), padx=5)
surname.grid(column=3, row=0,sticky=(N, W), padx=5)
ok.grid(column=4, row=0, sticky=(N, S, E, W))
tree.grid(column=0, row=1,columnspan=4, sticky=(N, S, E, W), padx=5)
prikazi.grid(column=4, row=1,sticky=(E, W))
osobelbl.grid(column=0,row=2,columnspan=4, sticky=(N, S, E, W))
name.focus()
root.bind("<Return>", unesiLice)
root.mainloop()