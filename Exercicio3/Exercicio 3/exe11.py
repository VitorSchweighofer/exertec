nome = input('Nome do asteroide: ')
distancia = float(input('Distancia do asteroide até a terra em KM: '))

if (distancia>768800):
	cor = str('verde')
if (distancia<768800) and (distancia>384400):
	cor = str('amarelo')
if (distancia<384400) and (distancia>38000):
	cor = str('laranja')
if (distancia<38000):
	cor = str('vermelho')
print ('O nome do asteróide é: %s' %(nome))
print ('Ele passará a %.2f km da terra' %(distancia))
print ('A sua categoria é %s' %(cor))


