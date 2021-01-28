ano = int(input('Digite o ano aqui: '))
bissexto = ano%4
if (bissexto==0):
	print('Esse ano é bissexto')
else:
	print('Não é bissexto')
