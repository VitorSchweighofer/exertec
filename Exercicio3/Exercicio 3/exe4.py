nome = input('digite seu nome aqui: ')
altura = float(input('digite sua altura aqui: '))
peso = float(input('digite seu peso aqui: '))
a = peso/(altura*altura)
if(a<18.5):
	print('Você está abaixo do peso, pois seu IMC é %.2f' %(a))
if((a>18.5)and(a<25)):
	print('Você está no peso normal, pois seu IMC é %.2f' %(a))
if((a>25)and(a<31)):
	print('Você está acima do peso, pois seu IMC é %.2f' %(a))
if(a>30):
	print('Você está obeso, pois seu IMC é %.2f' %(a))
