from ultimoexx.lib.interface import *
from ultimoexx.lib.arquivo import *
from time import sleep

arq = 'Text'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
        resp = menu(['Ver pessoas cadastradas','Cadastrar Pessoas','Sair do Sistema'])
        if resp == 1:
            lerArquivo(arq)
        elif resp == 2:
            cabeçalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = leiaint('Idade: ')
            cadastar(arq,nome,idade)
        elif resp == 3:
            cabeçalho('Saindo do Sistema... Até logo!')
            break
        else:
            print('\033[;31mERRO opçao inválida\033[m')
        sleep(2)

