number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))
number3 = int(input('Digite o terceiro número: '))
if (number1<number2<number3):
	print('%i é maior que %i que é maior que %i' %(number3, number2, number1))
if (number1<number3<number2):
	print('%i é maior que %i que é maior que %i' %(number2, number3, number1))
if (number2<number3<number1):
	print('%i é maior que %i que é maior que %i' %(number1,number3,number2))
if (number2<number1<number3):
	print('%i é maior que %i que é maior que %i' %(number3,number1,number2))
if (number3<number2<number1):
	print('%i é maior que %i que é maior que %i' %(number1,number2,number3))
if(number3<number1<number2):
	print('%i é maior que %i que é maior que %i' %(number2,number1,number3))
	