from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import os
from os.path import basename,splitext
browsedFiles=[]
def FileNameAndExt(filePath):
	y=os.path.basename(filePath)
	return(os.path.splitext(y))
def calculation():
	print (browsedFiles)
	#fileNames=map(os.path.splitext,browsedFiles)
	#fileNames=map(lambda x:splitext(basename(x)) ,browsedFiles)
	
	#By Beshin CAR
	fileNames = filter(lambda x: splitext(x)[1] == ".exe",browsedFiles)
	
	#By Beshin CAR
	#fileNames = [ x for x in browsedFiles if splitext(x)[1] == ".exe"]
	
	#fileNames=map(os.path.basename,browsedFiles)
	#fileNames= [os.path.basename(x) for x in browsedFiles ]
	for x in fileNames:
		print (x)
		#tree.insert("" , 0,values=(x[0],x[1]))

def fileDialogCallback():
	fname = askopenfilename(filetypes=(("All files", "*.*"), ))
	if fname:
		browsedFiles.append(fname)
	return
	
root = Tk()
content = ttk.Frame(root)
browse = ttk.Button(content, text="Browse", command=fileDialogCallback)
calcul = ttk.Button(content, text="File type", command=calculation)
tree = ttk.Treeview(content)
tree['show'] = 'headings'
tree["columns"]=("prva","druga")
tree.heading("prva", text="Fajl")
tree.heading("druga", text="Extenzija")
content.grid(column=0, row=0, sticky=(N, S, E, W))
browse.grid(column=0, row=0, sticky=(N, S, E, W))
calcul.grid(column=1, row=0, sticky=(N, S, E, W))
tree.grid(column=0, row=1,columnspan=4, sticky=(N, S, E, W), padx=5)
root.mainloop()