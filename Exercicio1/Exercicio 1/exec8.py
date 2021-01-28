#Uma das naves espaciais (uma sonda, na realidade) mais rápida já lançada ao espaço pela humanidade é a Voyager 1. Esta sonda já saiu da região de influência do Sol e foi a primeira sonda a chegar ao espaço interestelar. A velocidade da sonda é de 17km/s. Faça um programa (FUP) que imprima na tela em quanto tempo (em anos) esta sonda chegaria ao sistema Alpha Centaur
velocidadeLuz = 3*10**5
segundosEmUmAno = 60*60*24*365
distanciaAnoLuz = velocidadeLuz*segundosEmUmAno
distanciaEstrela = 4.24*distanciaAnoLuz
voyagerEmUmAno = segundosEmUmAno*17
tempoVoyagerAteEstrela = distanciaEstrela/voyagerEmUmAno
print('O tempo em anos que o voyager demoraria pra chegar no sistema alpha seria de %i' %(tempoVoyagerAteEstrela))