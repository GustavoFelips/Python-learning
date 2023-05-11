frase = ('Eu sou o cara')
print(frase[4:13:2])
# [onde começa : onde termna : pulos]
print(len(frase))
#lê quantos caracteres existem
print(frase.count('o',0,13))
#lê quanto há um string, começo e fim dos caracteres
print(frase.find('sou'))
#posição onde começa essa palavra
print('eu' in frase)
#confere se há string na variavel
print(frase.replace('cara','roberto carlos'))
#substitui uma frase por outra
print(frase.upper())
#transforma em maiúsculo
print(frase.lower())
#transforma em maiúsulo
print(frase.capitalize())
#Só a primeira letra em maiúculo
print(frase.title())
#depois do espaço a 1 letra fica em maiúscula
print(frase.strip())
#tira os esaços inúteis 'rstrip' para direita 'lstrip' para esquerda
print(frase.split())
#após o espaço recomeça a contagem, criando uma lista com as palavras
print('olá'.join(frase))