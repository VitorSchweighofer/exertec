antecessor = 0
numerofibonacci = 1
qtd = int(input('Quantos numeros gerar?'))

for contador in range(1,qtd+1):
	temp = numerofibonacci
	numerofibonacci = numerofibonacci + antecessor
	antecessor = temp
	print(numerofibonacci)