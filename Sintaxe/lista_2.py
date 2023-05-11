'''
            listas compostas
lista = [1,2]
numeros = []
numeros.append(lista[:])
numeros[0][1]
'''
'''
dados = list()
lista = list()
r = 's'
c = menor = maior = 0
while r == 's':
    lista.append(str(input('Qual o seu nome? ')))
    lista.append(float( input('Qual seu peso? ')))
    if len(dados) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor :
            menor = lista[1]
    r = str(input('Quer continuar? '))
    dados.append(lista[:])
    lista.clear()
    c+=1
print(f'você cadastrou {len(dados)} pessoas')
print(f'o maior peso foi o de ',end='')
for p in dados:
    if p[1] == maior:
        print(f'{p[0]} ',end='')
print()
print('o menor peso foi o de ',end='')
for p in dados:
    if p[1] == menor:
        print(f'{p[0]} ',end='')
'''
'''
todos = [[],[]]
for c in range(0,7):
    valor = (int(input('digite um numero: ')))
    if valor % 2 == 0:
        todos[0].append(valor)
    else :
        todos[1].append(valor)
todos[0].sort()
todos[1].sort()
print(f'os valores impares são: {todos[1]}')
print(f'os valores pares são: {todos[0]}')
'''
'''
s = s3 = maior = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'digite um valor para a posição [{l};{c}]'))
print('+='*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 ==0:
            s+=matriz[l][c]
        if c == 2:
            s3+=matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior or matriz[l][c] == maior:
                maior = matriz[l][c]
    print('\n')

print(f'A soma de todos os valores pares é {s}')
print(f'soma da 3º coluna {s3}')
print(f'o maior valor da 2ªlinha é {maior}')
'''
''' /// MEGA SENA ///
from time import sleep
from random import randint
mega = list()
jogo = list()
qtd = int(input('Quantos jogos serão gerados? '))
for jogos in range(0,qtd):
    for num in range(1,7):
        a = randint(0,60)
        while a in jogo:
            a = randint(0, 60)
        jogo.append(a)
    jogo.sort()
    mega.append(jogo[:])
    del jogo[:]
    sleep(1)
    print(f'jogo {jogos+1}: {mega[jogos]}')
'''
'''
boletin = list()
resp = 's'
cont = num = 0
while resp not in 'nN':
    aluno = str(input('Nome do aluno: '))
    nota1 = float(input('nota 1:'))
    nota2 = float(input('nota 2:'))
    media = (nota1+nota2)/2
    boletin.append([aluno,[nota1,nota2],media])
    resp = str(input('Quer continuar? '))
    cont+=1
print(f'{"Nº.":<4}{"NOME":<10}{"MEDIA":>6}')
for c in range(0,cont):
    print(f'{c:<4}{boletin[c][0]:<10}{boletin[c][2]:>6.1f}')
while num != 999:
    num = int(input('Mostrar notas de qual aluno? (999 para interromper)'))
    print(f'Notas de {boletin[num][0]} são {boletin[num][1]}')
'''