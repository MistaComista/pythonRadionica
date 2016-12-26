def nekaFja():
	print ("Ovo je neka fja")

def UnosIIspisImena(duzina):	
	imena=[]
	print(id(imena))
	potvrda='d'
	while potvrda=='d':
		ime=input("unesi ime: ")
		imena.append(ime)
		potvrda=input("za nastavak unesi 'd' ")
	print(imena)
	print(id(imena))
	duziOd=[]
	for i in imena:
		if len(i)>=duzina:
			duziOd.append(i)
	print("Imena duza od %s karaktera:" %(duzina))
	print(duziOd)
UnosIIspisImena(8)