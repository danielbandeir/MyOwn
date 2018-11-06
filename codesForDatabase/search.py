import sqlite3
from .login import login

lg = login()

class search():

    def verPessoas(self, nome):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * from user')
        row = c.fetchall()

        for rows in row:
            if rows[2] == nome:
                return [rows]
    
    def verPessoas(self, nome):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * from user')
        row = c.fetchall()

        for rows in row:
            if rows[2] == nome:
                return [rows]

    def verPessoasCont(self, id):
        
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * from friends WHERE id_User = ?', (id, ))
        row = c.fetchall()
        c.execute('SELECT * from user')
        pessoas = c.fetchall()
        persons = []
        for rows in row:
            for pessoa in pessoas:
                if rows[1] == pessoa[0]:
                    persons.append(pessoa)

        return persons

    def verPessoasContSearch(self, nome):
        
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        idS = lg.verLogado()
        c.execute('SELECT * from friends WHERE id_User = ?', (idS, ))
        row = c.fetchall()
        c.execute('SELECT * from user')
        pessoas = c.fetchall()
        persons = []
        for rows in row:
            for pessoa in pessoas:
                if rows[1] == pessoa[0]:
                    persons.append(pessoa)

        for pessoas in persons:
            if pessoas[2] == nome:
                return [pessoas]



    def verGrupos(self, nome):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * from grupo WHERE nome_grupo = ?',(nome, ))
        row = c.fetchall()
        
        if row:
            return row
        
        else:

            return None
    
    def verGruposID(self, id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * from grupo WHERE id_Grupo = ?',(id, ))
        row = c.fetchall()
        
        if row:
            return row
        
        else:

            return None

    
    def verTudoPessoas(self):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * from user')
        row = c.fetchall()

        return row
    

    def verTudoGrupos(self):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * from grupo')
        row = c.fetchall()

        return row
    
    def verMembroGrupoDates(self, id, busca):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()

        c.execute('SELECT * from membros_Grupo WHERE id_Grupo = ?',(id,))
        rows = c.fetchall()

        c.execute('SELECT * from user WHERE nome_user = ?',(busca,))
        rows2 = c.fetchall()

        for pessoa in rows:
            for usuario in rows2:
                if usuario[0] == pessoa[1]:
                   return usuario


    def verTudoGrupoDates(self, id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * from user')
        row = c.fetchall()

        c.execute('SELECT * from membros_Grupo WHERE id_Grupo = ?',(id,))
        rows = c.fetchall()

        pessoas = []

        for grupos in row:
            for membros in rows:
                if grupos[0] == membros[1]:
                    pessoas.append(grupos)

        return pessoas

    def verTudoGruposAdm(self):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * from grupo')
        row = c.fetchall()
        
        ids= lg.verLogado()

        c.execute('SELECT * from adm_Grupo WHERE id_User = ?',(ids,))
        rows = c.fetchall()

        for grupos in row:
            for adms in rows:
                if grupos[0] == adms[0]:
                    return [grupos]

    def addGrupo(self, idGrupo):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()

        idLogado = lg.verLogado()

        if self.verificarMembro(idGrupo):
            print('entrou errado1')
            return False
        else:
            try:
                print('entrou errado2')
                if not self.verificarSolicitacao(idGrupo):
                    c.execute('INSERT INTO solicitar_Grupo(id_Grupo, id_Solicitado, estado) VALUES(?,?,?)', (idGrupo, idLogado, 0))
                    conn.commit()
            except:
                print('entrou errado3')
                return True

        
    def verificarMembro(self, idGrupo):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()

        idLogado = lg.verLogado()
        c.execute('SELECT * FROM membros_Grupo WHERE id_User = ? AND id_Grupo = ?',(idLogado, idGrupo))
        row = c.fetchall()
        if row:
            return True
        else:
            return False
    
    def verificarSolicitacao(self, idGrupo):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()

        idLogado = lg.verLogado()
        c.execute('SELECT * FROM solicitar_Grupo WHERE id_Grupo = ? AND id_Solicitado = ?',(idGrupo, idLogado))
        row = c.fetchall()
        if row:
            if row[2] == 0:
                return True
            else:
                return False
        else:
            return False
            

    def verTodasPessoas(self):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()

        c.execute('SELECT * FROM user')
        row = c.fetchall()
        c.execute('SELECT * FROM solicitar_Grupo')
        rows = c.fetchall()

        for solicitacoes in rows:
            for pessoas in row:
                if solicitacoes[1] == pessoas[0]:
                    return [pessoas]

        