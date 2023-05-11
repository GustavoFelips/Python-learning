'''
def area(larg,comp):
    a = larg*comp
    print(f'A área de um terreno {larg}x{comp} é de {a:.2f}m²')


print()
print('  Controle de Terrenos  ')
print('-'*30)
l = float(input('LARGURA {m}: '))
c = float(input('COMPRIMENTO {m}: '))
area(l,c)
'''
'''
def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)


escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('Cev')
'''
'''
from time import sleep
def contado(inicio,fim,passo):
    if passo < 0:
        passo = -passo
    elif passo == 0:
        passo = 1
    print('-='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if fim > inicio:
        for c in range(inicio,fim+1,passo):
            print(c, end=' ', flush=True)
            sleep(0.6)
    elif inicio > fim:
        for c in range(inicio,fim-1,-passo):
            print(c, end=' ', flush=True)
            sleep(0.6)
    print('FIM!')


contado(1,10,1)
contado(10,0,2)
print('-='*30)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contado(i,f,p)
'''
'''
from time import sleep
def maior(*num):
    m = 0
    print('-='*30)
    print('ANALISANDO OS VALORES PASSADOS...')
    for a in num:
        print(a,end=' ')
        sleep(0.7)
        if a > m or m == 0:
            m = a
    print(f'foram informados {len(num)} valores ao todo.')
    print(f'O maior valor foi {m}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
'''
'''
from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ',end='')
    for c in range(0,6):
        lista.append(randint(0,10))
        print(lista[c],end=' ', flush=True)
        sleep(0.7)
    print('PRONTO!')


def soma(lista):
    s = 0
    print(f'Somando os valores pares de {lista}, ',end='')
    for i, c in enumerate(lista):
        if lista[i]%2 == 0:
            s+=lista[i]
    print(f'temos {s}')


numeros = list()
sorteia(numeros)
soma(numeros)
'''
