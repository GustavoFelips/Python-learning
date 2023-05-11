#sexo = str(input(' Qual seu sexo [F/M]: ')).upper()
#while sexo not in 'FM':
#        sexo = str(input(' sexo invalido, digite novamnte: ')).upper().strip()[0]
#print(f'sexo {sexo} informado com sucesso!')
#------------------------------------------------------------
#from random import randint
#import time
#n = 0
#a = randint(0,10)
#cont = 1
#print('-'*30)
#print('processando.........')
#print('-'*30)
#time.sleep(2)
#n = int(input('Em qual número o computador pensou (0-10)? '))
#while n != a:
#    n = int(input('você errou, tente novamente:  '))
#    cont+=1
#    if n > a:
#        print('dica: menos')
#        print('-'*20)
#    if n < a:
#        print('dica : mais')
#        print('-'*20)
#print('-'*20)
#print('você acertouuuuu ')
#print('-'*20)
#print(f'foram necessárias {cont} palpites!')
#---------------------------------------------------------
#v = 0
#n1 = int(input('Diz um número aí: '))
#n2 = int(input('Diz outro número aí: '))
#while v != 5:
#    print('O que você quer fazer com esses valore? ')
#    print('[1] para somar')
#    print('[2] para multiplicar')
#    print('[3] para maior')
#    print('[4] novos números ')
#    print('[5] para sair do programa')
#    v = int(input(': '))
#    if v == 1:
#        s = n1+n2
#        print(s)
#    elif v == 2 :
#        s = n1*n2
#        print(s)
#    elif v == 3 :
#        if n1 > n2:
#            print(f'o maior é {n1}')
#        else:
#            print(f'o maior é {n2}')
#    elif v == 4:
#        n1 = int(input('Diz um número aí: '))
#        n2 = int(input('Diz um número aí: '))
#    else:
#        print('\nerro\n')
#print('ok,thcau')
#--------------------------------------------
#f = int(input('fatorial so número: '))
#c = f
#t = 1
#print(f'{f}!= ',end='')
#while c > 0:
#    if c == 1:
#        print(f'{c}=',end='')
#    else:
#        print(f'{c}x', end='')
#    t = t * c
#    c -= 1
#print(f'{t}')
#--------------------------------------------------
#p = int(input('Primeiro termo da PA: '))
#r = int(input('A razão da PA: '))
#c = 1
#t = p
#total = 0
#mais = 11
#while mais != 0:
#    total = total + mais
#    while c < total :
#        print(f' O {c}ºtermo é {t}')
#        t = t+r
#        c+=1
#    mais = int(input('Quantos mais você quer ? '))
#print('FIM')
#------------------------------------
#n = int(input(' termos da sequencia : '))
#t1 = 0
#t2 = 1
#cont = 3
#print(f'{t1}~{t2}',end='')
#while cont <= n:
#    t3 = t2 + t1
#    print(f'~{t3}',end='')
#    t1 = t2
#    t2 = t3
#    cont+=1
#------------------------------------------
#cont = s = i = 0
#i = int(input('digite um número [999 para parar] '))
#while i != 999:
#    s = s + i
#    cont = +1
#    i = int(input('digite um número [999 para parar] '))
#print(f'a soma é {s}')
#print(f'froam digitados {cont} números ')
#--------------------------------------------
#d = 'sim'
#s = menor = maior = cont = 0
#j = 1
#while d == 'sim':
#    i = int(input('digite um número: '))
#    s = s + i
#    cont+=1
#    if cont == 1:
#        maior = menor = i
#    else:
#        if i < menor:
#            menor = i
#        if i > maior:
#            maior = i
#    d = str(input(' vc quer contnuar [sim/nao]? ')).strip().lower()
#m = s/cont
#print(f'a media é {m}')
#print(f' o menor numero e {menor}')
#print(f'o maior numero é {maior}')

#-------------------------------------
#----------INTERROMPER WHILE------------------------
#-------------------------------------------------------
#cont = s = 0
#while True:
#    n = int(input('Digite um número (999 para parar): '))
#    if n == 999:
#        break
#    s+=n
#    cont+=1
#print(f'A soma desses numero são : {s}')
#print(f'Foram digitados : {cont} números')
#-----------------------------------------------------
#n = 1
#while True:
#    print('-'*20)
#    n = int(input('Tabuada de qual número? '))
#    print('-'*20)
#    if n < 0:
#        print('FIM.')
#        break
#    for x in range(0,11):
#        print(f'{n}x{x}={n*x}')
#----------------------------------
#import random
#r = v = jogador = 0
#while True:
#    n = random.randint(0,10)
#    jogador = int(input('digite um número: '))
#    ip = str(input(' impar ou par? ')).strip().lower()
#    print('-' * 20)
#    r = n + jogador
#    if ip == 'par' and r%2 == 0 or ip == 'impar' and r%2 != 0 :
#        v+=1
#        print(f'o computador : {n}')
#        print('-'*20)
#        print(f'você : {jogador}')
#        print('-' * 20)
#        print(f'resultado : {r}\n \033[0;;44m você ganhouuu!! \033[m')
#        print('-' * 20)
#    elif ip == 'par' and r%2 != 0 or ip == 'impar' and r%2 == 0:
#        print(f'o computador : {n}')
#        print('-' * 20)
#        print(f'você : {jogador}')
#        print('-' * 20)
#        print(f'o resultado foi : {r} \n \033[0;;41m você perdeu \033[m')
#        break
#print('-' * 20)
#print(f'vitorias consecutivas = {v}')
#-------------------------------------------
#h = mm = d = 0
#while True:
#    idade = int(input('sua idade: '))
#    sexo = c = ' '
#    while sexo not in 'FM':
#        sexo = str(input('seu sexo [F\M]: ')).strip().upper()
#    while c not in 'SN':
#        c = str(input('você quer continuar? ')).strip().upper()
#    if idade > 18:
#            d+=1
#    if sexo == 'M':
#        h+=1
#    if sexo == 'F' and idade < 20:
#        mm+=1
#    if c == 'N':
#        break
#print(f'{d} pessoas tem +18')
#print(f'{h} homemns foram cadastrados')
#print(f'{mm} mulheres tem menos de 20 anos ')
#-----------------------------------------------------
#cont = s = m = b = 0
#barato = ''
#while True:
#    nome = str(input('Qual o nome do produto? ')).strip()
#    p = float(input('Qual o preço do produto? '))
#    cont+=1
#    if p > 1000:
#        m+=1
#    if cont == 1:
#        b = p
#        barato = nome
#    else:
#        if p < b:
#            b = p
#            barato = nome
#    c = str(input('Quer continuar? ')).strip().upper()
#    s+=p
#    if c == 'N':
#        break
#print('{:-^40}'.format(' fim do programa '))
#print(f'o total de gasto foi :R${s:.2f}')
#print(f'{m} produtos custam mais de R$1000')
#print(f'O produto mais barato é {barato}')
#---------------------------------------------------
#valor = int(input('Qual o valor sera sacado? '))
#total = valor
#ced = 50
#totced = 0
#while True:
    #if total >= ced:
    #    total -=ced
    #    totced+=1
    #else:
    #    if totced > 0 :
    #        print(f'total de {totced} de {ced}')
    #        ced = 20
    #    elif ced == 20:
    #        ced = 10
    #    elif ced == 10:
    #        ced = 1
    #    totced = 0
    #    if total == 0:
    #        break

