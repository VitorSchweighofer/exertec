#Calcule e imprima na tela a quantidade de esferas de 1,5 cm de raio que podem ser acomodadas em um cilindro de 12 cm de raio e 14 cm de altura. (Apresente somente a parte inteira da divisão, afinal não queremos colocar 0,2324 esfera dentro do cilindro, por exemplo).
import math
raioEsfera = 1.5
raioCilindro = 12
alturaCilindro = 14
volumeCilindro = alturaCilindro*math.pi*raioCilindro**2
volumeEsfera = 4/3*math.pi*raioEsfera**3
quantidadeDeEsferas = volumeCilindro/volumeEsfera
print('A quantidade de esferas que cabem dentro do cilindro é %i' %(quantidadeDeEsferas))