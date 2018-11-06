import sqlite3
from .login import login

lg = login()

class grupo():

    def verGrupos(self):
        idLogado = lg.verLogado()

        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()

        c.execute('SELECT * from grupo')
        row = c.fetchall()

        return row