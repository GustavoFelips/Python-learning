''' DICIONÁRIOS
CRIAR:
    dados = dict()
Acrescentar:
     dados['sexo'] = 'M'
remover:
    del dados['sexo']
EXEMPLO DICIONÁRIO:
filme{ 'título':'star wars',
    'ano':'1977',
    'diretor':'george lucas'
}
print(filmes.values()) - > retorna os valores do diconário
print(filmes.keys()) - > retorna os índices
print(filmes.items()) - > retorna ambos

REPETIÇÃO:
for k,v in filme.items()
    print(f'O {k} é {v}')
--- o titulo é estar wars
COPIAR ELEMENTO
estado = dict()
brasil = list()
brasil.append(estado.copy())
'''
'''
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}? '))
if aluno['media'] >= 6 :
    aluno['situação'] = 'aprovado'
else:
    aluno['situação'] = 'reprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
'''
'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),'jogador2':randint(1,6),'jogador3':randint(1,6),'jogador4': randint(1,6)}
ranking = list()
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*20)
print('== RANKING DOS JOGADORES ==')
for i,v in enumerate(ranking):
    print(f'{i+1}ª lugar : {v[0]} com {v[1]}')
'''
'''
from datetime import datetime
carteira = dict()
carteira['nome'] = str(input('Nome: '))
carteira['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
carteira['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if carteira['ctps'] != 0:
    carteira['contratação'] = int(input('Ano de contratação: '))
    carteira['salario'] = float(input('salário: R$ '))
    carteira['aposentado'] = (carteira['contratação'] + 35) - (2022 - carteira['idade'])
    print('-='*30)
for k,v in carteira.items():
    print(f'{k} tem o valor {v}')
'''
'''
aproveitamento = dict()
gols = list()
aproveitamento['nome'] = str(input('Nome do jogador: '))
p = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou? '))
for i in range(0,p):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
aproveitamento['gols'] = gols[:]
aproveitamento['total'] = sum(gols)
print('-='*30)
print(aproveitamento)
print('-='*30)
for k,v in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {aproveitamento["nome"]} jogou {p} partidas.')
for i, v in enumerate(aproveitamento["gols"]):
    print(f'      => na patida {i}, fez {v}')
print(f'Foi um totoal de {aproveitamento["total"]} gols.')
'''
'''
banco = list()
pessoa = {}
r = 's'
s = 0
while r not in 'nN':
    pessoa.clear()
    pessoa["nome"] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[F/M]: ')).upper()
        if pessoa["sexo"] in "FM":
            break
        print('ERRO! Digite apenas F ou M')
    pessoa['idade'] = int(input('Idade: '))
    s+=pessoa["idade"]
    banco.append(pessoa.copy())
    while True:
        r = str(input('Quer continuar? [S/N]')).upper()
        if r in 'SsNn':
            break
        print('ERRO! Responda apenas com S ou N')
media = s/len(banco)
print(f'- O grpo tem {len(banco)} pessoas')
print(f'- Média de idade do grupo é de {media} anos')
print(f'- As mulheres cadastradas foram: ',end='')
for b in banco:
    if b["sexo"] in 'fF':
        print(b["nome"],end=' ')
for a in banco:
    if a["idade"] > media:
        acima.append(a)
print(f'\n- Lista das pessoas que estão acima da média : ')
for b in banco:
    if b['idade'] >= media:
        print('   ',end='')
        for k,v in b.items():
            print(f'{k} = {v};',end=' ')
        print()
print('<< ENCERRADO >>')
'''
'''
clube = list()
aproveitamento = dict()
gols = list()
while True:
    gols.clear()
    aproveitamento.clear()
    aproveitamento['nome'] = str(input('Nome do jogador: '))
    p = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou? '))
    for i in range(0,p):
        gols.append(int(input(f'Quantos gols na partida {i}? ')))
    aproveitamento['gols'] = gols[:]
    aproveitamento['total'] = sum(gols)
    clube.append(aproveitamento.copy())
    while True:
        resp = str(input('Quer continuar? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas com S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(f'cod',end=' ')
for i in aproveitamento.keys():
    print(f'{i:<15}',end='')
print()
print('-='*40)
for k, v in enumerate(clube):
    print(f'{k:>3}',end=' ')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
prnt('-='*40)
while True:
    dados = int(input('Mostar dados de qual jogador? '))
    if dados == 999:
        break
    if dados >= len(aproveitamento):
        print(f'ERRO! Não existe jogador com ocódigo {dados}')
    else:
        print('-='*40)
        print(f'LEVANTAMENTO DO JOGADOR {clube[dados]["nome"]}')
        for i, d in enumerate(clube[dados]["gols"]):
            print(f'No jogo {i+1} fez {d} gols')
        print('-='*40)
print("<< VOLTE SEMPRE >>")
'''
