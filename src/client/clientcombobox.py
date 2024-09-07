from database import Database


def get_cityname(self):
    database = Database()

    if database.cursor.execute("SELECT city FROM city"):
        for rows in database.cursor.fetchall():
            self.city_combobox.configure(values=rows)
            return rows

    database.connection.close()



