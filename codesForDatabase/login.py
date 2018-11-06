import sqlite3
from ..model.database import createDatabase

class login():

    def verificarLogin(self, email, senha):
        conn = sqlite3.connect('./database/project.db')
        c = conn.cursor()
        c.execute('SELECT * FROM user')

        rows = c.fetchall()

        for row in rows:
            if row[1] == email and row[3] == senha:
                c.execute('INSERT INTO userLogado (id_User, estado_User) values(?,?)', (row[0], 1))
                conn.commit()
                return True
            else:
                continue
        
        c.close()

    def verificaLogado(self):
        conn = sqlite3.connect('./database/project.db')
        c = conn.cursor()
        c.execute('SELECT * from userLogado')

        rows = c.fetchall()
        if rows:
            for row in rows:
                if row[1] == 1:
                    return True
                else:
                    return False

    def verLogado(self):
        conn = sqlite3.connect('./database/project.db')
        c = conn.cursor()
        c.execute('SELECT * from userLogado')

        rows = c.fetchall()

        for row in rows:
            if row[1] == 1:
                return row[0]
                break
        