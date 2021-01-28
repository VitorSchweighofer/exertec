def dna():
    dna = open("C:\\Users\\Usuario\\Desktop\\dna\\vitor.txt","r")
    dna2 = dna.readlines()
    dna.close()

    trocar = str.maketrans("ACTG", "TGAC")
    comp = dna2[0].translate(trocar)
	
    print(dna2)
    print(comp)


dna()
