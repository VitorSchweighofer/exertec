listaCarros = []
listaConsumo = []
totalConsumo = 0
menorConsumo = 1000
maiorConsumo = 0
carroMaiorConsumo = []
carroMenorConsumo = []

while(True):
	carro = input("Digite o modelo do veículo: ")
	consumo = float(input("Digite o consumo do carro: "))
	listaCarros.append(carro)
	listaConsumo.append(consumo)
	mais = input("Adicionar mais um carro? (Sim/Não) ")
	if(mais.lower() == "não")
		break
for contador in range(0,len(listaCarros)):
	totalConsumo = totalConsmo+listaConsumo[contador]
	if(listaConsumo[contador]<menorConsumo):
		menor consumo = listaConsumo[contado]
		carroMenorConsumo=listaConsumo[contador]
	if(listaConsumo[contador]>maiorConsumo):
		maiorConsumo = listaConsumo[contador]
		carroMaiorConsumo = listaCarros[contador]
media = totalConsumo/len(listaCarros)
print("O consumo medio foi de %2.f" %(media))
print("O carro com maior consumo é %s !" %(carroMaiorConsumo))
print("O carro com menor consumo é %s !" %(carroMenorConsumo))