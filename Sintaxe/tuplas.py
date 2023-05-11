#tuplas são IMUTÁVEIS
# print(tupla[0:2])
#são string
#for c in tupla
#print(c)
#mostrará todos os elementos.
#a Tupla é representado por '( )'
#exemplo
#lanche = ('hamburguer','suco','pizza','pudim')
#print(lanche[:2])
#for comida in lanche:
#    print(f'eu vou comer {comida}')
#print(lanche.index('pizza'))
'''para ver onde esta o item'''
#print(sorted(lanche))
'''deixa em ordem'''
#tracin = ('-'*15)
#p = 0
#brasileirao = ('COR','AME','BGT','CAM','CFC','SAO','SAN',  'CLU','INT','AVA','PAL','FLA','BOT','FLU','CEA','CAP','ACG','GOI','JUV','FOR')
#print('Primeiros colocados :' )
#for primeiros in brasileirao[0:5]:
#    p+=1
#    print(f'{p}º lugar : {primeiros}')
#print(f'{tracin} em ultimos lugares {tracin}')
#for ultimos in brasileirao[16::]:
#    print(f'{brasileirao.index(ultimos)+1}°lugar: {ultimos}')
#print(f'{tracin} TIME EM ORDEM ALFABETICA {tracin}')
#for alpha in sorted(brasileirao):
#    print(alpha)
#print(tracin)
#print(f'O FLAMENGO ESTÁ EM {brasileirao.index("FLA")+1}ºLUGAAR')
#maior = 0
#menor = c = 0
#tupla2 =''
import random
#tupla = (random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5))
#print(tupla)
#while True:
#    n = random.randint(0,5)
#    tupla = n.__str__()
#    tupla2+=tupla
#    if n > maior or maior == 0 :
#        maior = n
#    elif n < menor or menor == 0:
#        menor = n
#    c+=1
#    if c == 5:
#        break
#print(tupla2)
#print(f'o maior valor é {maior}')
#print(f'o menor valor é {menor}')

#tupla = ('')
#p = 0
#for x in range(0,4):
#    v = int(input('diga-me um valor'))
#    tupla+=v.__str__()
#    if v%2 == 0 :
#        p+=1
#print(tupla[0::])
#if tupla.count('9') == 0:
#    print('nao há numero 9')
#else:
#    print(f'foram escritos {tupla.count("9")} vezes o numero noveº')
#print(f'foram escritos {p} numeros pares')
#print(tupla.index('3')+1)

#tupla = ('pao',0.50,'bolacha',2.00,'guaraná',6.00,'açucar',3.00,'açai',10.00)
#c = 1
#for n in tupla[::2]:
#    print(f'{n:.<20} R$ {tupla[c]:>6.2f}')
#    c+=2

#tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON')
#for palavra in tupla:
#    print(f'\nNa palavra {palavra} temos ',end='')
#    for letra in palavra:
#        if letra.lower() in 'aeiou':
#            print(letra.lower(),end=' ')

