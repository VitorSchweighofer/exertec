#A velocidade da luz no vácuo é constante e é de 3*105 km/s. A estrela mais próxima da terra (Sistema Alpha Centauri) fica a 4,24 anos-luz de distância. Calcule e imprima na tela a distância em KM até esta estrela.
velocidadeLuz = 3*10**5
segundosEmUmAno = 60*60*24*365
distanciaAnoLuz = velocidadeLuz*segundosEmUmAno
distanciaEstrela = 4.24*distanciaAnoLuz
print('A distancia da estrela é %i' %(distanciaEstrela))