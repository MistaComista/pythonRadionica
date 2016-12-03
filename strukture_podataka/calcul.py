#uneteReci izdvaja samo imena
def calcul():
	try:
		uneteReci=[elem[0] for elem in osobe]
		osobeVar.set(" ".join(uneteReci))
	except:
		pass