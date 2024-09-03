from sqlite3 import connect


class Database:
    def __init__(self):
        self.connection = connect("sqlite3.db")
        
        self.createtable_user()
        self.createtable_client()
        self.createtable_city()


    def createtable_user(self):
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS `user` (
                `id`        INTEGER UNSIGNED NOT NULL AUTOINCREMENT,
                `name`      TEXT NOT NULL
                `phone`     TEXT NOT NULL 
                `email`     TEXT NOT NULL 
                `username`  TEXT NOT NULL 
                `password`  INTEGER NOT NULL
           );
           
           ALTER TABLE `user` ADD PRIMARY KEY (`id`);
        """)
        
        self.connection.commit()
        self.connection.close()


    def createtable_client(self):
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS `client` (
                `id`        INTEGER UNSIGNED NOT NULL AUTOINCREMENT, 
                `name`      TEXT NOT NULL,
                `cpf`       TEXT NOT NULL,
                `birthdate` TEXT NOT NULL,
                `gender`    TEXT NOT NULL,
                `city_id`   INTEGER NOT NULL
            );
            
            ALTER TABLE `client` ADD PRIMARY KEY(`id`); 
            ALTER TABLE `client` ADD CONSTRAINT foreignkey_cityid FOREIGN KEY(`city_id`) REFERENCES `city`(`city_id`);
        """)
        
        self.connection.commit()
        self.connection.close()
                
                
    def createtable_city(self):
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS `city` (
                `id`    INTEGER UNSIGNED NOT NULL AUTOINCREMENT,
                `name`  TEXT NOT NULL,
                `state` TEXT NOT NULL
            );
            
            ALTER TABLE `city` ADD PRIMARY KEY(`id`);
        """)
        
        self.connection.commit()
        self.connection.close()
        

