morango = float(input('Insira a quantidade em kg dos morangos: '))
maça = float(input('Insira a quantidade em kg das maçãs: '))

if (morango<=5):
	morangoP = 2.5 * morango
if (maça<=5):
	maçaP = 1.8 * maça
if (morango>5):
	morangoP = 2.2 * morango
if (maça>5):
	maçaP= 1.5 * maça

valor = morangoP + maçaP
if (morango + maça>8) or (valor>25):
	valortotal = valor - (valor/10)
else:
	valortotal = valor
print ('O valor a ser pago pelo cliente é %.2f' %(valortotal))



	



