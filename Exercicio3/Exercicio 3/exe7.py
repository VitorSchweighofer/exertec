number = float(input('digite aqui o número: '))
resultado1 = number%2
resultado2 = number%3
resultado3 = number%5
if (((resultado1==0) and (resultado2==0)) and (resultado3==0)):
	print('O seu número é divisivel por 2,3 e 5')
if (resultado1>0):
	print('O seu número não passou no teste')
elif (resultado2>0):
	print('O seu número não passou no teste')
elif (resultado3>0):
	print('O seu número não passou no teste')
