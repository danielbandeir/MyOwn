import sqlite3
from .login import login
lg = login()

class logout():
    
    def deslogar(self):
        conn = sqlite3.connect('./database/project.db', check_same_thread=False)
        c = conn.cursor()
        
        c.execute('DELETE FROM userLogado WHERE estado_User = 1')
        conn.commit()
