from database import Database


def get_cityname(self):
    database = Database()

    if database.cursor.execute("SELECT city FROM city"):
        for rows in database.cursor.fetchall():
            self.city_combobox.configure(values=rows)
            return rows

    database.connection.close()


def insert_new_city(self):
    database = Database()

    if self.city_combobox != get_cityname:
        return database.cursor.execute("INSERT INTO city (city) VALUES ('" + self.city_combobox + "')")

    database.connection.close()



