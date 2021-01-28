numero1	= int(input('Digite o numero inferior aqui: '))
numero2 = int(input("Digite o numero superior aqui: "))
divisores = 0
if (numero1>numero2):
	print('O suposto limite inferior está maior que o superior')
for divisor in range(numero1, numero2+1):
	if (divisor == 2):
		print('2')
	if (divisor == 3):
		print ('3')
	if (divisor == 5):
		print ('5')
	if (divisor == 7):
		print ('7')
	if (divisor % 2 > 0) and (divisor % 3 >0) and (divisor % 5>0) and (divisor % 7 >0) and (divisor != 1):
		print('%i' %(divisor))