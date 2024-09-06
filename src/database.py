from sqlite3 import connect


class Database:
    def __init__(self):
        self.connection = connect("file:/../../sqlite3.db")
        self.cursor = self.connection.cursor()
        
        self.createtable_user()

    def createtable_user(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user (
                id        INTEGER PRIMARY KEY,
                name      TEXT,
                phone     TEXT,
                email     TEXT,
                username  TEXT, 
                password  INTEGER              
           );
        """)
