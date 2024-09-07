from sqlite3 import connect


class Database:
    def __init__(self):
        self.connection = connect("file:/../../sqlite3.db")
        self.cursor = self.connection.cursor()
        
        self.createtable_user()
        self.createtable_city()
        self.createtable_client()

    def createtable_user(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user (
                id        INTEGER PRIMARY KEY,
                name      TEXT,
                phone     TEXT,
                email     TEXT,
                username  TEXT, 
                password  TEXT              
           );
        """)

    def createtable_city(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS city (
                id      INTEGER PRIMARY KEY,
                city    TEXT,
                state   TEXT,
                country TEXT
            );
        """)

    def createtable_client(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS client (
                id        INTEGER PRIMARY KEY,
                name      TEXT,
                cpf       TEXT,
                birthdate TEXT,
                gender    TEXT,
                city   TEXT
            );
        """)
