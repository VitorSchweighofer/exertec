import unittest

num1 = int(input("Insira o número 1:"))
num2 = int(input("Insira o número 2:"))
num3 = int(input("Insira o número 3:"))

def maior(num1, num2, num3):
	if (num1 > num2 and num1> num3):
		print(num1)
		return num1
	if (num2 > num1 and num2 > num3):
		print(num2)
		return num2
	if (num3 > num1 and num3> num2):
		print(num3)
		return num3
maior(num1,num2,num3)

raio = float(input("Insira o raio:"))
altura = float(input("Insira a altura:"))
def cone(raio, altura):
	volume = 3.14*(raio*raio)*altura/3
	print(volume)
	return volume
cone(raio, altura)

palavra = input("Insira a palavra:")
def vogal(palavra):
	vogais=0
	for i in palavra:
		if i in "aeiouAEIOU":
			vogais = vogais+1
	print(vogais)
	return vogais
vogal(palavra)

class teste(unittest.TestCase):
	def testemaior(self):
		self.assertEqual(maior(1,2,3),3)

	def testecone(self):
		self.assertEqual(cone(4,12),200.96)

	def testavogal(self):
		self.assertEqual(vogal("aeiouAEIOU"),10)

if __name__ == '__main__':
   unittest.main()