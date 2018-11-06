import sqlite3
from .login import login

lg = login()

class profile():

    def addPerson(self, id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * from user')
        row = c.fetchall()

        c.execute('SELECT * from solicitar_Friend')
        rows2 = c.fetchall()

        idLogado = lg.verLogado()

        if self.saoAmigos(id):
            print('são amigos')
            return False
        else:
            if not self.verificarAmizade(id):
                c.execute('INSERT INTO solicitar_Friend(id_User, id_Solicitado, estado) VALUES(?,?,?)', (id, idLogado, 0))
                conn.commit()
                return True
    
    def saoAmigos(self, id):
        idLogado = lg.verLogado()
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * from friends WHERE id_User = ? and id_Friend = ?',(id ,idLogado))
        row = c.fetchall()
        c.execute('SELECT * from friends WHERE id_User = ? and id_Friend = ?',(idLogado ,id))
        rows = c.fetchall()

        if rows or row:
            print('São amigos')
            return True
        else:
            return False

    def verificarAmizade(self, id):
        idLogado = lg.verLogado()
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * from solicitar_Friend WHERE id_User = ? and id_Solicitado = ?',(id ,idLogado))
        row = c.fetchall()
        c.execute('SELECT * from solicitar_Friend WHERE id_User = ? and id_Solicitado = ?',(idLogado ,id))
        row2 = c.fetchall()

        if row:
            for rows in row:
                if rows[2] == 0:
                    print('Tentando ja a amizade')
                    return True
        if row2:
            for rows in row2:
                if rows[2] == 0:
                    print('Tentando ja a amizade')
                    return True
        else:
            return False
    
    def verDados(self, id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * from user WHERE id_User = ?', (id,))
        row = c.fetchall()

        return row

