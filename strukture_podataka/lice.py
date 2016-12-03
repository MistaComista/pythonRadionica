from tkinter import *
from tkinter import ttk
import tkinter.messagebox

def ubaci_ime(*args):

        try:
            lista.insert("","end",text=(brojv.get()),values=(imev.get(),prezimev.get()))
            imev.set("")
            prezimev.set("")
            brojv.set("")
            broj.focus()
        except:
            tkinter.messagebox.showerror("Greška","Unesite podatke pravilno")
            imev.set("")
            prezimev.set("")
            brojv.set("")
            broj.focus()


def brisi(*args):
    red=lista.selection()[0]
    lista.delete(red)




koren=Tk()
imev = StringVar()
prezimev = StringVar()
brojv=IntVar()
brojv.set("")

koren.title("Imenik")
prozor=ttk.Frame(koren, padding=(3,3,3,3))
prozor.grid(row=0, column=0)
prozor.columnconfigure(0, weight=100)
prozor.rowconfigure(0, weight=100)
lista=ttk.Treeview(prozor,columns="heder")
lista.grid(row=3, column=0, columnspan=6,sticky=(N+W+S+E))
lista["columns"]=("jedan","dva")
lista.column("jedan")
lista.column("dva")
lista.heading("jedan",text="Ime")
lista.heading("dva",text="Prezime")
lista.heading("#0",text="R.B")
brojlbl=ttk.Label(prozor,text="Broj")
brojlbl.grid(row=0,column=0)
broj=ttk.Entry(prozor,textvariable=brojv)
broj.grid(row=0,column=1)
imelbl=ttk.Label(prozor, text="Ime")
imelbl.grid(row=0, column=2)
ime=ttk.Entry(prozor, textvariable=imev)
ime.grid(row=0, column=3)
prezimelbl=ttk.Label(prozor, text="Prezime")
prezimelbl.grid(row=0, column=4)
prezime=ttk.Entry(prozor, textvariable=prezimev)
prezime.grid(row=0, column=5)
dugme=ttk.Button(prozor, text="Unos", command=ubaci_ime)
dugme.grid(row=0,column=6)
dugme2=ttk.Button(prozor, text="Obriši red", command=brisi)
dugme2.grid(row=3,column=6)
prazno=ttk.Label(prozor)
prazno.grid(row=2)
koren.columnconfigure(0, weight=1)
koren.rowconfigure(0, weight=1)


for child in koren.winfo_children():
    child.grid_configure(padx = 20, pady = 20)

broj.focus()
koren.bind("<Return>", ubaci_ime)
koren.bind("<Delete>", brisi)

koren.mainloop()
