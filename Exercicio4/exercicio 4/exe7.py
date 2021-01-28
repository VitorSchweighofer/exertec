numeroLimite = int(input('Digite o limite aqui: '))
for multiplos in range (numeroLimite,-1,-1):
	if multiplos % 7 == 0:
		print(multiplos)