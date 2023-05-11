''' TRATAMENTO DE ERROS

try: - > Tentar fazer uma operção

execpt: - > Caso a tentativa dê erro
execpt (ValueErros,TypeError): - > DEFINE O TIPO DE ERRO
    print('Tivemos um problema com os  tipos de dados que você digitou')
execpt Exception as erro: - > Mostra qula foi o erro
    print(f'problema encontrado foi {erro.__class__}')

else - > Caso a tentativa seja feita

finally: - > Irá acontecer sempre, mesmo se der certo ou errado\


'''

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('\033[;31m O usúario preferiu não digitar\033[m')
            n = 0
            break
        except:
            print('\033[;31m ERRO! Escreva um número decimal\033[m')
        else:
            break
    return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except KeyboardInterrupt:
            print('\033[;31m O usúario preferiu não dgitar esse número\033[m')
            n = 0
            break
        except:
            print('\033[;31m ERRO! digite um número real válido.\033[m')
        else:
            break
    return n


i = leiaint('Digite um número inteiro: ')
f = leiafloat('Digite um número decimal: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f}')

'''
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não esrá acecessível no momento')
else:
    print('Consegui acessar o site pudim')
'''

