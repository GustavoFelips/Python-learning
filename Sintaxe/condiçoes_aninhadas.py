#v = float(input('Valor da casa: R$'))
#s = float(input('salário do comprador: R$'))
#a = float(input('quantos anos para ele pagar? '))
#pm = v/(12*a)
#l = 0.30*s
#if pm > l:
#    print('empréstimo foi cancelado')
#else:
#    print('o emprestimo foi aceito')
#--------------------------------------
#i = int(input('diga-me um numero inteiro: '))
#c = int(input('Escolha a base de conversaçao (1,2 ou 3): '))
#if c == "1":
#
#elif c == '2':
#
#elif == '3':
#
#else:
#    print('nemhuma opção escolhida.')

#n = int(input('digite numero : '))
#n1 = int(input('digite numero : '))
#if n > n1:
#    print(f'o numero {n} é maior que o numero {n1}')
#elif n < n1:
#    print(f'{n1} é maior que o {n}')
#else:
#    print('os doi valores sao iguais')

#n = int(input('digite o ano do seu nascimeto: '))
#a = 2022 - n
#if a > 18 :
#    print('voce ja deveria ter se alistado')
#    t = a - 18
#    if t < 2:
#        print(f'ha {t} ano atrás')
#    else:
#        print(f'ha {t} anos atrás')
#elif a < 18 :
#    print('voce ainda irá se alistar')
#    t = 18 - a
#    if t < 2:
#        print(f'daqui a {t} ano')
#    else:
#        print(f'daqui a {t} anos')
#else:
#    print("já é hora de se alistar")
#---------------------------------------
#n1 = float(input('nota 1: '))
#n2 = float(input('nota 2: '))
#m = (n1+n2)/2
#if m < 5:
#    print('reprovado')
#elif m in range(5,7):
#    print('recuperaçao')
#elif m >= 7:
#    print("APROVADO!!")
#---------------------------------------
#r1 = float(input('comprimento do 1ªsegmento: '))
#r2 = float(input('comprimento ddo 2ªsefmento:'))
#r3 = float(input('comprimento d0 3ª segmento: '))
#if r1 <= (r2-r3):
#    print('esse triangulo nao pode existir')
#else:
#    print('esse triangulo existe')
#    if r1 == r2 and r2 == r3:
#        print('Triangulo Equilataro')
#    elif r1 == r2 or r2 == r3 or r2 == r3:
#        print('Triangulo Isósceles')
#    else:
#        print('Triangulo Escaleno')
#---------------------------------------------------
#p = float(input('preço do produt0: R$'))
#c = int(input("forma de pagamento \n 1 - dinheiro/chque \n 2 - cartão"))
#if c == 1:
#    pn = 0.90*p
#    print(f'o valor com 10% de desconto fica R%{pn}')
#elif c == 2:
 #   x = int(input('1 para pagar ávista \n 2 para parcelar em 2x \n 3 para parcelar em 3x ou mais\n'))
 #   if x == 1:
 #       pn = 0.95*p
 #       print(f'o valor fica {pn} com 5% de desconto')
 #   elif x== 2:
 #       print(f'o preço fica {pn}')
 #   elif x == 3:
 #       pn = 1.20*p
 #       print(f'o valor fica {pn} com ')
 #---------------------------------------------------
import random
joken = ('pedra', 'papel', 'tesoura')
comp = random.randint(0,2)
joga = int(input("[0] pedra\n[1] papel\n[2] tesoura\n"))
if joga == 0:
    if comp == 0:
        print(f'o computador jogou {joken[comp]}')
        print('deu empate')
    elif comp == 1:
        print(f'o computador jogou {joken[comp]}')
        print('você ganhooou')
    elif comp == 2:
        print(f'o computador jogou {joken[comp]}')
        print('vc ganhouuu')
elif joga == 1:
    if comp == 0:
        print(f'o computador jogou {joken[comp]}')
        print('você gnahouuu')
    elif comp == 1:
        print(f'o computador jogou {joken[comp]}')
        print('Empate')
    elif comp == 2:
        print(f'o computador jogou {joken[comp]}')
        print('você perdeu')
elif joga == 2 :
    if comp == 0:
        print(f'o computador jogou {joken[comp]}')
        print('você perrdeu')
    elif comp == 1:
        print(f'o computador jogou {joken[comp]}')
        print('você ganhooou')
    elif comp == 2:
        print(f'o computador jogou {joken[comp]}')
        print('empate')