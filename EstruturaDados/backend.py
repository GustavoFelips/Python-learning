import sqlite3 as sql

class TrasactionObject():
    database = "users.db"
    conn = None
    cur = None
    conected = False

    def connect(self):
        TrasactionObject.conn = sql.connect(TrasactionObject.database)
        TrasactionObject.cur = TrasactionObject.conn.cursor()
        TrasactionObject.conected = True

    def disconnect(self):
        TrasactionObject.conn.close()
        TrasactionObject.conected = False

    def execute(self,sql,parms = None):
        if TrasactionObject.conected:
            if parms == None:
                TrasactionObject.cur.execute(sql)
            else:
                TrasactionObject.cur.execute(sql,parms)
                return True
        else:
            return False

    def fetchall(self):
        return TrasactionObject.cur.fetchall()

    def persist(self):
        if TrasactionObject.conected:
            TrasactionObject.conn.commit()
            return True
        else:
            return False

def initDB():
    trans = TrasactionObject()
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
    trans.persist()
    trans.disconnect()

def insert(nome,sobrenome,email,cpf):
    trans = TrasactionObject()
    trans.connect()
    trans.execute("INSERT INTO users VALUES (NULL,?,?,?,?)",(nome, sobrenome, email, cpf))
    trans.persist()
    trans.disconnect()


def view():
    trans = TrasactionObject()
    trans.connect()
    trans.execute("SELECT * FROM users")
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def search(nome="",sobrenome="",email="",cpf=""):
    trans = TrasactionObject()
    trans.connect()
    trans.execute("SELECT * FROM users WHERE nome=? or sobrenome=? or email=? or cpf=?",(nome,sobrenome,email,cpf))
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def delete(id):
    trans = TrasactionObject()
    trans.connect()
    trans.execute("DELETE FROM users WHERE id=?", (id,))
    trans.persist()
    trans.disconnect()

def update(id,nome,sobrenome,email,cpf):
    trans = TrasactionObject()
    trans.connect()
    trans.execute("UPDATE users SET nome=?, sobrenome=?, email=?,cpf=? WHERE id = ?",(nome,sobrenome,email,cpf,id))
    trans.persist()
    trans.disconnect()

initDB()