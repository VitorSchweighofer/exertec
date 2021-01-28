number1 = float(input('Primeiro número: '))
number2 = float(input('Segundo número: '))
print ('Escolha uma operação')
print ('Adição = 1')
print ('Subtração = 2')
print ('Multiplicação = 3')
print ('Divisão = 4')
print ('Raiz = 5')
print ('Potenciação = 6')

escolha = input('Digite sua escolha aqui: ')


if (escolha == '1'):
	resultado = number1 + number2
if (escolha == '2'):
	resultado = number1 - number2
if (escolha == '3'):
	resultado = number1 * number2
if (escolha == '4'):
	resultado = number1 / number2
if (escolha == '5'):
	resultado = number1 // number2
if (escolha == '6'):
	resultado = number1 ** number2
print ('O resultado de sua conta é {}' .format(resultado))