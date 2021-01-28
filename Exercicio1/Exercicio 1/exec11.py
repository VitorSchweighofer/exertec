#DESAFIO: A galáxia de Andrômeda situa-se a aproximadamente 2,9 milhões de anos-luz da terra, e sabe-se que ela se aproxima da Via Láctea (a nossa galáxia) à uma velocidade de 500 mil km por hora. FUP que mostre na tela o tempo que resta (em anos)  até o choque da galáxia de Andrômeda com a Via Láctea.
velocidadeLuz = 3*10**5
segundosEmUmAno = 60*60*24*365
distanciaAnoLuz = velocidadeLuz*segundosEmUmAno
distanciaAndromeda = 3*distanciaAnoLuz
velocidadeAndromeda = 500000
tempoRestante = distanciaAndromeda/velocidadeAndromeda
print('O tempo restante até que andromeda alcance é %i anos' %(tempoRestante))