import sqlite3

class createDatabase():
    
    def user(self):
        conn = sqlite3.connect('./database/project.db')
        c = conn.cursor()
        c.execute('PRAGMA foreign_keys = ON')
        c.execute('CREATE TABLE IF NOT EXISTS user(\
            id_User INTEGER PRIMARY KEY AUTOINCREMENT,\
            email_user varchar(100) NOT NULL,\
            nome_user varchar(100) NOT NULL,\
            senha_user varchar(100) NOT NULL,\
            foto_user varchar(255),\
            cidade_user varchar(100) NOT NULL,\
            aniversario varchar(100) NOT NULL,\
            sexo varchar(100) NOT NULL,\
            visibilidade INTEGER NOT NULL\
        )')

        c.execute('CREATE TABLE IF NOT EXISTS userLogado(\
            id_User INTEGER NOT NULL,\
            estado_User INTEGER NOT NULL,\
            FOREIGN KEY(id_User) REFERENCES user(id_User) ON DELETE CASCADE\
        )')
    
        c.execute('CREATE TABLE IF NOT EXISTS friends (\
            id_User INTEGER NOT NULL,\
            id_Friend INTEGER  NOT NULL,\
            FOREIGN KEY(id_User, id_Friend) REFERENCES user(id_User, id_User) ON DELETE CASCADE\
        )')

        c.execute('CREATE TABLE IF NOT EXISTS solicitar_Friend (\
            id_User INTEGER NOT NULL,\
            id_Solicitado INTEGER NOT NULL,\
            estado INTEGER NOT NULL,\
            FOREIGN KEY(id_User, id_Solicitado) REFERENCES user(id_User, id_User) ON DELETE CASCADE\
        )')

        c.execute('CREATE TABLE IF NOT EXISTS mural (\
            id_Mural INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            id_User INTEGER NOT NULL,\
            FOREIGN KEY(id_User) REFERENCES user(id_User) ON DELETE CASCADE\
        )')


        c.execute('CREATE TABLE IF NOT EXISTS mural_Grupo (\
            id_Mural INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            id_Grupo INTEGER NOT NULL,\
            id_User INTEGER NOT NULL,\
            FOREIGN KEY(id_Grupo) REFERENCES grupo(id_Grupo) ON DELETE CASCADE\
        )')


        c.execute('CREATE TABLE IF NOT EXISTS grupo (\
            id_Grupo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            nome_grupo varchar(100) NOT NULL,\
            desc_grupo VARCHAR(150) NOT NULL,\
            foto_grupo varchar(255),\
            visibilidade_grupo varchar(255) NOT NULL\
        )')


        c.execute('CREATE TABLE IF NOT EXISTS post (\
            id_Post INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            id_User INTEGER NOT NULL,\
            id_Mural INTEGER NOT NULL,\
            texto_Mural varchar(255),\
            foto_Mural varchar(255),\
            FOREIGN KEY(id_Mural) REFERENCES mural(id_Mural) ON DELETE CASCADE,\
            FOREIGN KEY(id_User) REFERENCES user(id_User) ON DELETE CASCADE\
        )')


        c.execute('CREATE TABLE IF NOT EXISTS post_Grupo (\
            id_Post INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            id_User INTEGER NOT NULL,\
            id_Mural INTEGER NOT NULL,\
            texto_Mural varchar(255),\
            foto_Mural varchar(255),\
            FOREIGN KEY(id_Mural) REFERENCES mural(id_Mural) ON DELETE CASCADE,\
            FOREIGN KEY(id_User) REFERENCES user(id_User) ON DELETE CASCADE\
        )')


        c.execute('CREATE TABLE IF NOT EXISTS comment (\
            id_Coment INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            id_Post INTEGER,\
            comentario varchar(255) NOT NULL,\
            id_User INTEGET NOT NULL,\
            FOREIGN KEY(id_Post) REFERENCES post(id_Post) ON DELETE CASCADE, \
            FOREIGN KEY(id_User) REFERENCES user(id_User) ON DELETE CASCADE\
        )')

        c.execute('CREATE TABLE IF NOT EXISTS comment_Grupo (\
            id_Coment INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            id_Post INTEGER,\
            id_User INTEGET NOT NULL,\
            comentario varchar(255) NOT NULL,\
            FOREIGN KEY(id_Post) REFERENCES mural_Grupo(id_Post) ON DELETE CASCADE,\
            FOREIGN KEY(id_User) REFERENCES user(id_User) ON DELETE CASCADE\
        )')


        c.execute('CREATE TABLE IF NOT EXISTS resposta (\
            id_Resposta INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            id_Coment INTEGER,\
            resposta_Coment varchar(255) NOT NULL,\
            id_User INTEGER,\
            FOREIGN KEY(id_Coment) REFERENCES coment(id_Coment) ON DELETE CASCADE\
        )')

        c.execute('CREATE TABLE IF NOT EXISTS resposta_Grupo (\
            id_Resposta INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
            id_Coment INTEGER,\
            resposta_Coment varchar(255) NOT NULL,\
            id_User INTEGER,\
            FOREIGN KEY(id_Coment) REFERENCES coment_Grupo(id_Coment) ON DELETE CASCADE\
        )')

        c.execute('CREATE TABLE IF NOT EXISTS membros_Grupo (\
            id_Grupo INTEGER NOT NULL,\
            id_User INTEGER NOT NULL ,\
            FOREIGN KEY(id_Grupo) REFERENCES grupo(id_Grupo) ON DELETE CASCADE,\
            FOREIGN KEY(id_User) REFERENCES user(id_User) ON DELETE CASCADE\
        )')

        c.execute('CREATE TABLE IF NOT EXISTS adm_Grupo (\
            id_Grupo INTEGER NOT NULL,\
            id_User INTEGER NOT NULL ,\
            FOREIGN KEY(id_Grupo) REFERENCES grupo(id_Grupo) ON DELETE CASCADE,\
            FOREIGN KEY(id_User) REFERENCES user(id_User) ON DELETE CASCADE\
        )')

        c.execute('CREATE TABLE IF NOT EXISTS block_Membros (\
            id_Grupo INTEGER NOT NULL,\
            id_User INTEGER NOT NULL ,\
            estado_Block INTEGER NOT NULL,\
            FOREIGN KEY(id_Grupo) REFERENCES grupo(id_Grupo) ON DELETE CASCADE,\
            FOREIGN KEY(id_User) REFERENCES user(id_User) ON DELETE CASCADE\
        )')

        c.execute('CREATE TABLE IF NOT EXISTS block_Friend (\
            id_Friend INTEGER NOT NULL,\
            id_User INTEGER NOT NULL ,\
            estado_Block INTEGER NOT NULL,\
            FOREIGN KEY(id_Friend) REFERENCES user(id_user) ON DELETE CASCADE,\
            FOREIGN KEY(id_User) REFERENCES user(id_User) ON DELETE CASCADE\
        )')
        
        c.execute('CREATE TABLE IF NOT EXISTS block_Friend (\
            id_Grupo INTEGER NOT NULL,\
            id_User INTEGER NOT NULL ,\
            estado_solicitacao INTEGER NOT NULL,\
            FOREIGN KEY(id_Grupo) REFERENCES grupo(id_Grupo) ON DELETE CASCADE,\
            FOREIGN KEY(id_User) REFERENCES user(id_User) ON DELETE CASCADE\
        )')

        c.execute('CREATE TABLE IF NOT EXISTS solicitar_Grupo (\
            id_Grupo INTEGER NOT NULL,\
            id_Solicitado INTEGER NOT NULL,\
            estado INTEGER NOT NULL,\
            FOREIGN KEY(id_Solicitado) REFERENCES user(id_User) ON DELETE CASCADE,\
            FOREIGN KEY(id_Grupo) REFERENCES user(id_Grupo) ON DELETE CASCADE\
        )')
        
        conn.commit()
    