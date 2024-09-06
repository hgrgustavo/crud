from tkinter import messagebox
from database import Database


class CityCrud:
    def __init__(self, city_id, city: str, state: str, country: str):
        self.id = city_id
        self.city = city
        self.state = state
        self.country = country

    def insert(self) -> messagebox:
        database = Database()

        try:
            database.cursor.execute("insert into city (city, state, country) values ('" + self.city + "', '" + self.state + "', '" + self.country + "')")
            database.connection.commit()
            database.connection.close()

            return messagebox.showinfo("", "Cidade cadastrada com sucesso!")

        except:
            return messagebox.showwarning("", "Erro ao cadastrar cidade!")


    def delete(self) -> messagebox:
        database = Database()

        try:
            database.cursor.execute("delete from city where id = '" + self.id + "'")
            database.connection.commit()
            database.connection.close()

            return messagebox.showinfo("", "Cidade excluída com sucesso!")

        except:
            return messagebox.showwarning("", "Erro ao excluir cidade!")


    def update(self) -> messagebox:
        database = Database()

        try:
            database.cursor.execute("update city set city = '" + self.city + "', state = '" + self.state + "', country = '" + self.country + "' where id = '" + self.id + "'")
            database.connection.commit()
            database.connection.close()

            return messagebox.showinfo("", "Cidade atualizada com sucesso!")

        except:
            return messagebox.showwarning("", "Erro ao atualizar cidade!")

    def select(self, city_id) -> messagebox:
        database = Database()

        try:
            database.cursor.execute("select * from city where id = '" + city_id + "'")
            database.connection.commit()
            database.connection.close()

            data = []

            for row in data:
                self.id = row[0]
                self.city = row[1]
                self.state = row[2]
                self.country = row[3]

            return messagebox.showinfo("", "Busca feita com sucesso!")

        except:
            return messagebox.showwarning("", "Erro ao buscar cidade!")