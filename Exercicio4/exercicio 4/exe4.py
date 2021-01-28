numero = int(input('Digite aqui seu número: '))
tabuada = numero*1
print (tabuada)
for contador in range(1,10):
	number = tabuada
	tabuada = number + numero
	print(tabuada)