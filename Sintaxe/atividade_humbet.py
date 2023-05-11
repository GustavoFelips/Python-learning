'''1º) Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''
''' 1º
h = float(input('Qual a sua altura? '))
s = str(input('Qual seu sexo? \n[M] - Masculino\n[F] - Feminino \n:')).upper()
if s == 'M':
    peso_ideal = (72.7*h) - 58
    print(f'Seu peso ideal é : {peso_ideal:.2f}KG')
elif s == 'F':
    peso_ideal = (62.1*h) - 44.7
    print(f'Seu peso ideal é : {peso_ideal:.2f}KG')
'''
'''
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
'''
''' 2º
sal_hora = float(input('Quanto você recebe por hora? '))
horas = float(input('Quantas horas você trabalhou no mês? '))
sal_bruto = (sal_hora * horas)
fgts = sal_bruto*0.11
sindi = sal_bruto*0.03
if sal_bruto <= 900:
    imp = 0
    sal_liq = sal_bruto - sindi
elif sal_bruto <= 1500 and sal_bruto > 900:
    imp = sal_bruto*0.05
    sal_liq = (sal_bruto - imp) - sindi
elif sal_bruto > 1500 and sal_bruto <= 2500:
    imp = sal_bruto * 0.10
    sal_liq = (sal_bruto-imp) - sindi
elif sal_bruto > 2500:
    imp = sal_bruto * 0.20
    sal_liq = (sal_bruto-imp) - sindi
print(f'sálario bruto: R$ {sal_bruto}')
print(f'FGTS: R$ {fgts}')
print(f'Sindicato:R$ {sindi}')
print(f'Imposto de renda: R$ {imp} ')
print(f'Sálario líquido: R$ {sal_liq}')
'''
''' 3ª
vetor = list()
par = list()
impar = list()
for x in range(0,20):
    vetor.append(int(input('Digite um valor: ')))
    if vetor[x] % 2 == 0:
        par.append(vetor[x])
    else:
        impar.append(vetor[x])
print(f'todos: {vetor}')
print(f'pares : {par}')
print(f'impares : {impar}')
'''
''' 4ª
dia = int(input('Qual do dia do seu nascimento? '))
mes = int(input('Qual do mês do seu nascimento? '))
ano = int(input('Qual do ano do seu nascimento? '))
meses = {1:'janeiro',2:'fevereiro',3:'março',3:'abril',5:'maio',6:'junho',7:'julho',8:'Agosto',9:'setembro',10:'outubro',11:'novembro',12:'Dezembro'}
print(meses.get(mes))
'''
'''
r1 = float(input('comprimento do 1ªsegmento:'))
r2 = float(input('comprimento do 2ªsefmento:'))
r3 = float(input('comprimento do 3ª segmento:'))
if r1 <= (r2-r3) or r2 <= (r1-r2) or r3 <= (r1-r2):
    print('esse triangulo não pode existir')
else:
    print('esse triangulo existe')
    if r1 == r2 and r2 == r3:
        print('Triangulo Equilataro')
    elif r1 == r2 or r2 == r3 or r2 == r3:
        print('Triangulo Isósceles')
    else:
        print('Triangulo Escaleno')
'''