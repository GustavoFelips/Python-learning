#PADRÃO ANSI
#estrutura = \033[style;text;back m
#style = [0 = none ; 1 = bold ; 4 = underline ; 7 = negative]
#text = [30 = branco ; 31 = red ; 32 = verrde ; 33 = amarelo; 34 = azul; 35 = roxo; 36 = cian; 37 = marron]
#back-ground = [40; 41; 42; 43; 44; 45; 46; 47] mesmas cores do de cima

print('\033[1;31m ola, mundo!')
print('\033[4;30;45mfundao mané\033[m')
print('eu amo {}você{}!!'.format('\033[4;34m','\033[m'))
print('{}aboborinha{}'.format('\033[7;41m','\033[m'))


