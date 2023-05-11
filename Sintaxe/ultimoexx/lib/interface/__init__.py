def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print('\033[;31m O usúario preferiu não digitar\033[m')
        else:
            break
    return n

def linha(tam = 42):
    return '-'*tam


def cabeçalho(text):
    print(linha())
    print(text.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    opc = leiaint('Sua Oppção: ')
    return opc

