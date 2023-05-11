''' \\\ INTERACTIVE HELP \\\

- > help()
(Infoma sobre os parametros)
- > Descobrir os atributos
- pritn(help(input))
ou, porém difente
- print(input.__doc__)

\\\  DOCSTRINGS \\\
- > É a documentação
    - Para criar só basta por 3 aspas e falar sobre os parametros de uma def , por exemplo
    - Aparecerá quando o help for usado

\\\ PARÂMETROS OPCIONAIS \\\
- > Caso não haja um valor para o parãmetro
EXEMPLO:
    def somar(a,b, c = 0)
        s = a+b+c
        print(f'a soma vale {s}')


    somar(8,4)
    - > ou seja , não exite valor para c, então será 0

\\\ ESCOPO DE VARIÁVEIS \\\

- > Váriavel local : só exitirá dentro da função

- > Váriavel Global : existirá em todo o código

- > para usar a Váriavel global dentro de uma função
    def teste(b):
        global a
        a = 5

    a = 9 - > somente essa será usado

\\\ RETORNANDO VALORES \\\

def somar(a=0,b=0,c=0):
    s = a+b+c
    return s
- > Ou seja, a função se tornará um valor
EXEMPLO:
    resp = somar(4,7)
    print(f'As somas são {somar(3,4)}, {somar(1,1,1)} e {somar(9)}')
'''
'''
from datetime import datetime

def voto(ano):
    atual = datetime.now().year
    idade = atual - ano
    if 16 <= idade < 18 or idade >=65:
        return f'com {idade} anos: VOTO OPCIOAL'
    elif idade > 18:
        return f'com {idade} anos: VOTO OBRIGÁTORIO'
    else:
        return  f'com {idade} anos : NÃO VOTA'


nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
'''

'''
def fatorial(n,show=False):
    
    -> Calcula o Faatorial de um número.
    :param n: O número a ser calculado.
    :param show: [opcional] Mostar ou não a conta
    :return: O valor do Fatorial de um número n.
    
    f = 1
    for c in range(n,0,-1):
        if show == True:
            print(f'{c} ',end='')
            if c > 1:
                print('x ',end='')
            else:
                print(f'=',end=' ')
        f *= c
    return f

print(fatorial(5))
print(fatorial(5,show=True))
help(fatorial)
'''
'''
def ficha(nome='<Desconhecido>',gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do Jogador: '))
g = str(input('Nome de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)
'''
'''
def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('\033[;31m ERRO! Escreva um número inteiro\033[m')
    return n


n = leiaint('digite um número: ')
print(f'Você acabou de digitar o número {n}')
'''
'''
def notas(*num,still=False):

    -: Função para analisar notar  e situações de vários alunos
    :param num: uma ou mais notas dos alunos (aceita vários)
    :param still: Valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma

    info = dict()
    info['total'] = len(num)
    info['maior'] = max(num)
    info['menor'] = min(num)
    info['media'] = sum(num)/len(num)
    if still:
        if info['media'] > 6:
            info['Situação'] = 'BOA'
        elif 7 < info['media'] >= 6:
            info['Situação'] = 'RAZOÁVEL'
        else:
            info['Situação'] = 'RUIM'
    return info


resp = notas(1,2,3,4,still=True)
print(resp)
'''
'''
def ajuda(com):
    titulo(f'Acessando o manual de comamndo \'{com}\'', 4)
    print(cores[5])
    help(com)
    print('\033[m',end='')

def titulo(msg,cor=0):
    tam = len(msg)+4
    print(cores[cor],end='')
    print('~'*tam)
    print(f' {msg} ')
    print('~'*tam)
    print('\033[m',end='')


cores =  ["\033[7;40m",#branco
          "\033[41m",#red
          "\033[42m",#verde
          "\033[43m",#amarelo
          "\033[44m",#azul
          "\033[30;45m",#roxo
          "\033[46m",#cian
          "\033[47m"]#marrom
while True:
    titulo('SISTEMA DE AJUDA PYHELP',6)
    com = str(input('Função ou blibioteca > ')).lower()
    if com == 'fim':
        break
    else:
        ajuda(com)
titulo('ATÉ LOGO',2)
'''
