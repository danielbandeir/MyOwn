import sqlite3
from .login import login

lg = login()

class solicitacao():

    def verPessoas(self):
        conn = sqlite3.connect('./database/project.db')
        c = conn.cursor()
        idS = lg.verLogado()
        c.execute('SELECT * FROM solicitar_Friend where id_User = ? ', (idS, ))
        rows = c.fetchall()
        c.execute('SELECT * FROM user')
        rowsUser = c.fetchall()
        rowPerson = []

        for row in rows:
            for rowAdd in rowsUser:
                if row[1] == rowAdd[0]:
                    rowPerson.append((row[1], rowAdd[2], rowAdd[4]))

    

        return rowPerson
    
    def addPessoa(self, id):
        conn = sqlite3.connect('./database/project.db')
        c = conn.cursor()
        idS = lg.verLogado()

        if self.verAmizade(id):
            return False
        else:
            c.execute('INSERT INTO friends (id_User, id_Friend) VALUES(?,?)', (idS, id))
            c.execute('INSERT INTO friends (id_User, id_Friend) VALUES(?,?)', (id, idS))
            c.execute('DELETE FROM solicitar_Friend WHERE id_User = ? AND id_Solicitado = ?', (idS, id))
            conn.commit()
    
    def addPessoaGrupo(self, id, idGrupo):
        conn = sqlite3.connect('./database/project.db')
        c = conn.cursor()

        c.execute('INSERT INTO membros_Grupo (id_Grupo, id_User) VALUES(?,?)', (idGrupo, id))
        c.execute('DELETE FROM solicitar_Grupo WHERE id_Grupo = ? AND id_Solicitado = ?', (idGrupo, id))
        conn.commit()

    def RemovPessoaGrupo(self, id, idGrupo):
        conn = sqlite3.connect('./database/project.db')
        c = conn.cursor()

        c.execute('DELETE FROM solicitar_Grupo WHERE id_Grupo = ? AND id_Solicitado = ?', (idGrupo, id))
        conn.commit()

    def RemovPessoaGrupo2(self, id, idGrupo):
        conn = sqlite3.connect('./database/project.db')
        c = conn.cursor()

        c.execute('DELETE FROM membros_Grupo WHERE id_Grupo = ? AND id_User = ?', (idGrupo, id))
        conn.commit()

    def verAmizade(self, id):
        conn = sqlite3.connect('./database/project.db')
        c = conn.cursor()
        idS = lg.verLogado()

        c.execute('SELECT * FROM friends WHERE id_User = ? AND id_Friend = ?',(idS, id))
        row = c.fetchall()
        c.execute('SELECT * FROM friends WHERE id_User = ? AND id_Friend = ?',(id, idS))
        rows = c.fetchall()

        if row or rows:
            return True
        else:
            return False

    

