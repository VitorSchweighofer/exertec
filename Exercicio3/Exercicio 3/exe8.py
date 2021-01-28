a = float(input('Insira o primeiro lado do triangulo: '))
b = float(input('Insira o segundo lado do triangulo: '))
c = float(input('Insira o terceiro lado do triangulo: '))

if ((b - c) < a < b + c):
	if (a==b==c):
		print('Seu triangulo é equilátero')
	elif (a!=b!=c):
		print('Seu triangulo é escaleno')
	elif (a!=b) or (a!=c) or (b!=c):
		print('Seu triangulo é isósceles')
else:
	print('Não é possível ser um triangulo')