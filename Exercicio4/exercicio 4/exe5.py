numero = int(input('Digite um numero aqui: '))
divisores = 0
for divisor in range (1, numero):
	if numero % divisor == 0:
		divisores += 1
		print('O numero %i é divisivel por %i' %(numero, divisor))
		if (divisores>1):
			break
if (divisores>1):
	print ('O numero %i não é primo!' %(numero))
else:
	print ('O numero %i é primo' %(numero))
	