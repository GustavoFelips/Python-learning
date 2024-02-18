import sqlite3

conexao = sqlite3.connect("dados.bd")
cursor = conexao.cursor()

cursor.execute("CREATE TABLE contato(nome, endereco, telefone)")

res = cursor.execute("SELECT nome FROM sqlite_master")
res.fetchone()