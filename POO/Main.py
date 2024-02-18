'''Definições POO'''
# Classes : conjunto de atributos e funções utilizados como modelo para um objeto
# Objetos : Instância de uma classe. Possui as mesmas características comuns ás classes, porém com valores diferentes.
# Abstração: Acesso ás utilidades da classe. Ação de mensagem para utilizar os recursos de uma classe.
# Atributos : caraterísticas da classe
# Funções : Ação do objeto com retorno
# Metódos : Ação do objeto sem retorno
# Exceções de erros: Tratamento de erros
# Mensagem: Chamada a um atributo, metódo ou função
# Herança : Super classe e Sub Classe. Uma classe pode herdar atributos, métodos e/ou funções de outra.
# Encapsulamento : Níveis de acesso. O encapsulamento permite que os atributos sejam vistos somente nas classes onde foram declarados, definindo o nível de acesso de atributos, métodos ou funções.
# Polimorfismo : Sobrescrita. Escolher entre metódos, atributos e funções que sobrescreveram ou que foram sobrescritas

'''Nomenclatura'''
# Classes
# Referente a caracteres, seguir o mesmo padrão de variáveis e objetos.
# Sempre iniciar as classes com caracteres maiúsculos, inclusive as iniciais de nomes compostos:
# Exemplo: MinhaClasse()

# Variáveis e Objetos
# Utilizar somente caracteres e letras minúsculas.
# No caso de variáveis com nome composto, utilizar o underline para separação das palavras.
# Não iniciar o nome com números (podemos utilizar números no nome, mas não devemos iniciar com eles).
# Não utilizar caracteres especiais.
# Não utilizar espaçamento em branco.
# Evitar utilizar os caracteres I e O.

# Pacotes , Módulos e Métodos
# Utilizar nomes pequenos.
# Utilizar sempre caracteres minúsculos.
# Utilizar o underline para unir nomes compostos.

'''Encapsulamento'''
# Public
# Permite acesso tanto dentro quanto fora da classe. "_" na frente do nome
# Protected
# Somente classes e subclasses terão acesso. Uso do "_" antes do nome
# Private
# Permite somente a sua classe onde foi definido tenha acessoa adeterminado atributo ou método. Uso do "__' na frente do nome.

'''Métodos de Acesso'''
# Getters
# Retorna um valor. Usado para ler os valores da classe e enviá-los como retorno de função
# Setters
# Recebem valores por parâmetro. Recebem argumento que serão atribuidos a membro internos do objeto

'''Decorator'''
# Um decorator é um padrão de projeto de software que permite adicionar comportamento a um objeto já existente, em tempo de execução, ou seja, agrega, de forma dinâmica, responsabilidades adicionais a um objeto.
# Na prática, o decorator permite que atributos de uma classe tenham responsabilidades.
# Um decorator é um objeto invocável, uma função que aceita outra função como parâmetro (a função decorada).
# O decorator pode realizar algum processamento com a função decorada e devolvê-la ou substituí-la por outra função

'''Properaty'''
# A linguagem Python traz uma outra solução para manter os atributos privados, conhecida como Property.
# A função Property é um Decorator e é utilizada para obter um valor de um atributo.
# Basicamente, a função Property permite que você declare uma função para obter o valor de um atributo.

#Instanciando
from  Cliente import Cliente
from Conta import Conta
class Main:
    pass

print("testando...")
cliente1 = Cliente("Gustavo","99404-7270")
#print(cliente1)
#print(f"nome : {cliente1.nome}, Telefone : {cliente1.telefone}")

conta1 = Conta(cliente1.nome, 1010, 0)
#print(conta1)
#print(conta1.saldo)
#conta1.saldo = 10
#print(conta1.saldo)
conta1.deposito(10)
conta1.saque(5)
print(conta1.saldo)