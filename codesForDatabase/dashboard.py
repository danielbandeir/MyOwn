import sqlite3
from .login import login

lg = login()

class dashboard():
    def pegarDados(self, id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * from user')
        row = c.fetchall()

        for rows in row:
            if rows[0] == id:
                return rows

    def verificaMural(self, id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * FROM mural WHERE id_User = ?',(id, ))

        rows = c.fetchall()
        if rows:
            for row in rows:
                if row[1] == id:
                    break
        else:
            c.execute('INSERT INTO mural (id_User) values (?)', (id,))
            conn.commit()
        
        return True

    def idMural(self,id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * FROM mural')
        rows = c.fetchall()

        id = lg.verLogado()

        for row in rows:
            if row[1] == id:
                return row[0]
            else:
                continue
        
    def idMural2(self,id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * FROM mural WHERE id_User = ?',(id, ))
        rows = c.fetchall()

        for idSS in rows:
            return idSS[0]

        

    def registrarPost(self, id, image, text, id_User):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        idmural = self.idMural(id)

        c.execute('INSERT INTO post(id_User, id_Mural, texto_Mural, foto_Mural) values (?,?,?,?)', (id_User, idmural, text, image))
        conn.commit()

    def mostrarPosts(self, id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        idM = self.idMural(id)
        row = c.execute('SELECT * FROM post WHERE id_mural=?',(idM, ))

        return row
    
    def mostrarPosts2(self, id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        idM = self.idMural2(id)
        print (idM)
        row = c.execute('SELECT * FROM post WHERE id_Mural=? AND id_User = ?',(idM, id))
        print("idmsao",idM,"testa",id)

        for postagens in row:
            print(postagens)

    def registrarComent(self, text, id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        idS = lg.verLogado()
        idmural = self.idMural(id)

        c.execute('INSERT INTO comment(id_Post, comentario, id_User) values (?,?,?)', (id, text, idS))
        conn.commit()
        c.close()


    def pegarIdPost(self, text):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * FROM post WHERE texto_Mural = ?',(text, ))
        row = c.fetchall()
        for rows in row:
            return rows[0]

    def pegarPosts(self,id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * FROM post WHERE id_User=?',(id,))
        rows = c.fetchall()

        for post in rows:
            return post[0]


    def pegarComments(self):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * FROM comment')
        rows = c.fetchall()

        return rows

    def pegarResp(self):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * FROM resposta')
        rows = c.fetchall()

        return rows
    
    def registrarResp(self, text, id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        idS = lg.verLogado()
        idmural = self.idMural(id)

        c.execute('INSERT INTO resposta(id_Coment, resposta_Coment, id_User) values (?,?,?)', (id, text, idS))
        conn.commit()
        c.close()

    def pegarPessoas(self):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * FROM user')
        rows = c.fetchall()

        return rows


    def removerComent(self, id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON')
        c.execute('DELETE FROM comment WHERE id_Coment = ?',(id, )) 
        conn.commit()

    def verificaIdMural(self, id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute(' SELECT * FROM mural_Grupo WHERE id_Grupo = ? ',(id, ))
        row = c.fetchall()

        if row:
            return row[0]
        
        else:
            c.execute('INSERT INTO mural_Grupo(id_Grupo) VALUES(?) ',(id))


    

    def registrarPost3(self, id, image, text):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        idmural = self.idMural(id)

        c.execute('INSERT INTO post_Grupo(id_User, id_Mural, texto_Mural, foto_Mural) values (?,?,?,?)', (id, idmural, text, image))
        conn.commit()

    def registrarComent3(self, text, id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        idS = lg.verLogado()
        idmural = self.idMural(id)

        c.execute('INSERT INTO comment_Grupo(id_Post, comentario, id_User) values (?,?,?)', (id, text, idS))
        conn.commit()
        c.close()
    
    def registrarResp3(self, text, id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        idS = lg.verLogado()
        idmural = self.idMural(id)

        c.execute('INSERT INTO resposta(id_Coment, resposta_Coment, id_User) values (?,?,?)', (id, text, idS))
        conn.commit()
        c.close()

    def verGrupoDS(self, id):   
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * FROM grupo WHERE id_Grupo = ?',(id,))
        row = c.fetchall()
        return row


    def pegarPosts3(self,id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * FROM post_Grupo WHERE id_Mural=?',(id,))
        rows = c.fetchall()

        for post in rows:
            return post[0]


    def pegarComments3(self):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * FROM comment_Grupo')
        rows = c.fetchall()

        return rows

    def pegarResp3(self):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * FROM resposta_Grupo')
        rows = c.fetchall()

        return rows


        

    def pegarPessoas3(self, id):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * FROM membros_Grupo WHERE id_Grupo = ?', (id, ))
        rows = c.fetchall()
        c.execute('SELECT * FROM user')
        row = c.fetchall()

        for pessoas in row:
            for membros in rows:
                if membros[1] == pessoas[0]:
                    return pessoas