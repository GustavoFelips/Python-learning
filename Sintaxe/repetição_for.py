#range(inicio,fim,passo)
#for c in range(0,10,1):
#    print(c)
#s = 0
#for c in range(0,5):
#    n = int(input('digite um numero'))
#    s += n
#print(s)
#------------------------ATIVIDADESSS-----------------------------
#from time import sleep
#for c in range(10,-1,-1):
#    sleep(0.5)
#    print(c)
#print('BUM!!! BUM!! PAW!!')
#-----------------------------
#print('Todos os números pares entre 1 e 50 são: ')
#for c in range(0,51,2):
#    print(c)
#--------------------------------------
#s = 0
#v = 0
#print('soma dos numeros impares multiplos de 3 : ')
#for c in range(0,501,3):
#    if c%2 > 0:
#        v += 1
#        s += c
#print(f'a soma dos {v} valores são {s}')
#----------------------------------------------
#t = int(input('Tabuada do número : '))
#for c in range(0,11):
#    print(f'{t}x{c} = {t*c}')
#-----------------------------------
#s = 0
#for c in range(0,6):
#    n = int(input('diga-me um number: '))
#    if n%2 == 0 :
#        s+=n
#print(f'A soma dos numeros pares são : {s}')
#-----------------------------------------------------------
#t1 = int(input('Primeiro termo dessa PA: '))
#r = int(input('Razao dessa PA: '))
#termos = 2
#print('os 10 primeiros termos dessa PA: ')
#print(f'1ªtermo = {t1}')
#for c in range(1,11):
#    print(f'{termos}ºtermo = {t1+r*c}')
#    termos +=1
#------------------------------------------
#i = int(input('numero inteiro : '))
#cont = 0
#for c in range(1,10):
#    if i%c == 0:
#        cont+= 1
#if cont < 3:
#        print(f' o numero {i} é um numero primo')
#else:
#    print('é um numero par')
#------------------------------------------
#M = 0
#m = 0
#for x in range(0,7):
#    a = int(input('Qual o seu ano de nascimento? '))
#    i = 2022 - a
#    print(i)
#    if i < 21 :
#        M += 1
#    elif i >= 21:
#        m += 1
#print(f'{M} pessoas ainda nã0 atingiram a maioridade!\n')
#print(f'E {m} pessoas ja atingiram a maioridade')
#-------------------------------------------------------------------
#maior = 0
#menor = 0
#for x in range(0,5):
#    peso = float(input('Qual o seu peso ? '))
#    if x == 1:
#        maior = peso
#        menor = peso
#    else:
#        if peso > maior:
#            maior = peso
#        if peso < menor :
#            menor = peso
#print(f'o maior peso é o de {maior}kg')
#print(f'o menor peso é o de {menor}kg')
#-------------------------------------------
#velho = 0
#nomevelho = ''
#cont = 0
#idadetotal = 0
#for x in range(1,5):
#    nome = str(input('qual o seu nome? '))
#    sexo = str(input('qual seu sexo? (M/F): ')).strip().upper()
#    idade = int(input('qual o sua idade? '))
#    idadetotal+=idade
#    if idade > velho and sexo == 'M' :
#        velho = idade
#        nomevelho = nome
#    if sexo == 'F' and idade > 20:
#        cont+=1
#media = idadetotal/4
#print(f' a media de idade é {media}')
#print(nomevelho)
#print(f'exisitem {cont} mulheres com menos de 20 anos')
#---------------------------------------------------------



