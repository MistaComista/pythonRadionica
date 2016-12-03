potvrda='d'
imena=[]
while potvrda == 'd':
	ime=input("Unesite ime: ")
	print ('Uneli ste ime: %s ' %(ime))
	imena.append(ime)
	potvrda = input("Da li zelite da nastavite? ")
print (imena)