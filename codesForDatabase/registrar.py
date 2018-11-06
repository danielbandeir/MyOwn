import sqlite3
from .login import login

lg = login()

class registrar():
    conn = sqlite3.connect('./database/project.db', check_same_thread=False)

    def registrarBanco(self, email, nome, senha, foto, cidade, aniversario, sexo, visibilidade=1):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON;')
        c.execute('INSERT INTO user(email_user, nome_user, senha_user, foto_user, cidade_user, aniversario, sexo, visibilidade) VALUES(?,?,?,?,?,?,?,?)', (email, nome, senha, foto, cidade, aniversario, sexo, visibilidade))
        conn.commit()
        return True

    def registrarGrupo(self, nome, desc, foto, visibilidade=1):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON;')
        c.execute('INSERT INTO grupo(nome_grupo, desc_grupo, foto_grupo, visibilidade_grupo) VALUES(?,?,?,?)', (nome, desc, foto, visibilidade))
        conn.commit()
        
        idLogado = lg.verLogado()

        c.execute('SELECT * FROM grupo WHERE nome_grupo = ?',(nome, ))
        row = c.fetchall()

        if row:
            for linhas in row:
                c.execute('INSERT INTO adm_Grupo(id_Grupo, id_User) VALUES(?,?)',(linhas[0], idLogado))
                c.execute('INSERT INTO membros_Grupo(id_Grupo, id_User) VALUES(?,?)',(linhas[0], idLogado))
                conn.commit()
                return True
                