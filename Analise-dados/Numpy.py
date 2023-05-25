import numpy

#Criação de arrays
# array() -> cria uma matriz com os valores específicados
n = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(n)
# .shape() - > para saber a matriz (linha, coluna)
print(f'shape: {n.shape}')

# zeros((0, 0 )) - > cria uma matriz de zeros de acordo com os args(linha, coluna)
a = numpy.zeros((1, 2))
print(a)

# eye(0) - > Cria uma matriz identidade
a = numpy.eye(5)
print(a)

# numpy.random.random(()) - > Cria uma matriz com números aleatórios
a = numpy.random.randint(100, size=(2, 2))
b = numpy.random.random((2, 2))
print(a)

# numpy.linspace(inicio,final,num) - > cria um vetor com num elementos dentro do intervalo inical e final
a = numpy.linspace(0, 10, 11)
print(a)

# helpe(função) - > para saber como funciona uma função
#help(numpy)

#INDEXAÇÃO
#Indexação dessa forma mantém relação com a matriz original
A = numpy.array([[1, 2, 3], [4, 5, 6]])
B = A[:2,:2]
B[0, 0] = 8

#Remodelar uma matriz
#.reshape(linha, coluna)
C = A.reshape(1,-1)

#OPERAÇÕES ARITMÉTRICAS
# Elemento por elemento
x = numpy.random.randint(10, size=(3, 3))
y = numpy.random.randint(10, size=(3, 3))
print(x, '\n\n',y)
print('\n\n', x+y) # ou numpy.add(x,y)
print('\n\n', x-y) # ou numpy.subtract(x,y)
print('\n\n', x*y) # ou numpy.multiply(x, y)
print('\n\n', x/y) # ou numpy.divide(x, y)

#Multiplicação matriciais
print(x @ y)  # ou numpy.dot(x,y) , ou x.dot(y)

#Comparações feitas pelos operadores lógicos e retorna uma matriz lógica
print(x > y)

#indexação booleana
#Filtra os elementos da matriz
x = numpy.array([[1, 5, 3], [3, 2, 1], [4, 5, 6]])
cond = x >= 5
D = x[cond]
print(D)

#Metódo x.T transpõem linhas e colunas
print(x)
print('\n')
print(x.T)

#Soma dos elementos podendo ser por  linhas ou colunas, retornando um vetor
print(x)
print('\n')
print(numpy.sum(x))
print('\n')
print(numpy.sum(x, axis=0))
print('\n')
print(numpy.sum(x, axis=1))


#Média dos elementos
print(x)
print('\n')
print(numpy.mean(x))
print('\n')
print(numpy.mean(x,axis=0))
print('\n')
print(numpy.mean(x,axis=1))

#Identificação do indíce onde dada condição
condi = x % 2 == 0
print('condição:\n', condi)
i, j = numpy.where(condi)
print("Indíce i (linhas): ", i)
print("Indíce j (colunas): ", j)

#Mostra em que linhas a condição é verdadeira
print(numpy.sum(condi,axis=1))
print(numpy.where(numpy.sum(condi,axis=1))[0])



