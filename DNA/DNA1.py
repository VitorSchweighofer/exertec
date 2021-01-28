def DNA ():
	dna = open("C:\\Users\\Usuario\\Desktop\\dna\\vitor.txt","r")
	dna2 = dna.readlines()
	letraA = dna2[0].count("A")
	letraT = dna2[0].count("T")
	letraC = dna2[0].count("C")
	letraG = dna2[0].count("G")
	print(f"Quantidade de letras C: {letraC}")
	print(f"Quantidade de letras G: {letraG}")
	total = letraA+letraC+letraG+letraT
	totalCG = letraC+letraG
	porcentagem = (totalCG*100)/total
	print(f'{porcentagem}%')
	dna.close()
DNA()
dna = None
