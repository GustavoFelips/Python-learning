'''ADICIONAR NA LISTA
.append() - ADICIONA POR ULTIMO
.insert(0,'p') - POSIÇAO E VALOR
    REMOVER DA LISTA
del lista[]
.pop() - REMOVE O ULTIMO
.remove('p') - PEDE O VALOR
'''
#posimenor=''
#valores = []
#maior = menor = 0
#for c in range(0,5):
#    valores.append(int(input('digite um valor ')))
#    if valores[c] > maior or maior == 0:
#        maior = valores[c]
#        posimaior = c
#    if valores[c] < menor or menor == 0:
#        menor = valores[c]
#        posimenor = c
#print(f'o maior valor e {maior} na posiçao ',end='')
#for i, n in enumerate(valores):
#    if n == maior:
#        print(f'{i}...',end='')
#print(f'\no menor valor é {menor} na posiçao ',end='')
#for i, n in enumerate(valores):
#    if n == menor:
#        print(f'{i}...',end=' ')
'''
lista =  []
while True:
    n = int(input('digite um numero '))
    if n in lista:
        print('numero duplicado')
    else:
        print('número adicionado...')
        lista.append(n)
    r = str(input('quer continuar? ')).upper()
    if r == 'N':
        lista.sort()
        print(f'A lista é {lista}')
        break
'''
#-------------------------------------------------------------------
'''
lista = []
for c in range(0,5):
    n = int(input('digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'foi adicionado no final')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'foi adicionado na posição {pos}')
                break
            pos+=1
print(lista)
'''
#-------------------------------
'''
r = 's'
lista = []
while r == 's':
    lista.append(int(input('digite um número: ')))
    r = str(input('quer continuar? '))
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'a lista é {lista}')
if (5) in (lista):
    print('Há o numero 5 nas posições: ',end='')
    for i, c in enumerate(lista):
        if c == 5:
            print(f'{i}....',end='')
else:
    print('O valor 5 nao foi encontrado na lista')
'''
'''
r = 's'
lista = []
pares = []
impares = []
while r == 's':
    lista.append(int(input('digite um numero: ')))
    r = str(input('Quer continuar? '))
for i,p in enumerate(lista):
    if p%2 == 0:
        pares.append(p)
    else:
        impares.append(p)
print(f'lista completa : {lista}')
print(f'lista dos pares: {pares}')
print(f'lista ímpar: {impares}')
'''
'''
e = str(input('digite a expressão: '))
pilha = []
for simb  in e:
    if simb == '(':
        pilha.append(simb)
    elif simb == ')':
        if len(pilha) > 0:
            pilha.append(simb)
        else:
            pilha.pop()
if len(pilha) == 0:
    print('expressão correta')
else:
    print('expressão inválida')
'''