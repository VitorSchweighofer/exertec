valorhora = float(input('Insira quanto é o valor a sua hora: '))
horas = float(input('Insira a quantidade de horas trabalhadas no mês: '))

salariobruto = valorhora * horas
Inss = salariobruto/10
Fgts = salariobruto/9.09

if (salariobruto <= 900):
	porcentagem = 0
	Ir = 0
if (salariobruto >900) and (salariobruto<=1500):
	porcentagem = 5
	Ir = salariobruto/20
if (salariobruto >1500) and (salariobruto<=2500):
	porcentagem = 10
	Ir = salariobruto/10
if (salariobruto > 2500):
	porcentagem = 20
	Ir = salariobruto/5

totaldesconto = Ir + Inss
salarioliquido = salariobruto - totaldesconto

print ('________________________________')
print ('|Salário Bruto (%.0f*%.0f)| %.2f|' %(valorhora,horas,salariobruto))
print ('________________________________')
print ('|(-) IR (%.0f%%)          | %.2f  |' %(porcentagem,Ir))
print ('________________________________')
print ('|(-) INSS (10%%)       | %.2f |' %(Inss))
print ('________________________________')
print ('|FGTS (11%%)           | %.2f |' %(Fgts))
print ('________________________________')
print ('|Total de descontos   | %.2f |' %(totaldesconto))
print ('________________________________')
print ('|Salário Liquido      | %.2f |' %(salarioliquido))
print ('________________________________')