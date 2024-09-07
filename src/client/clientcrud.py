from tkinter import messagebox
from database import Database


class ClientCrud:
    def __init__(self, client_id, name: str, cpf: str, birthdate: str, gender: str, city: str):
        self.id = client_id
        self.name = name
        self.cpf = cpf
        self.birthdate = birthdate
        self.gender = gender
        self.city = city

    def insert(self) -> messagebox:
        database = Database()

        try:
            database.cursor.execute(
                "INSERT INTO client (id, name, cpf, birthdate, gender, city) VALUES ('" + self.id + "', '" + self.name + "', '" + self.cpf + "', '" + self.birthdate + "', '" + self.gender + "', '" + self.city + "')")
            database.connection.commit()
            database.connection.close()

            return messagebox.showinfo("", "Cliente cadastrado com sucesso!")

        except:
            return messagebox.showwarning("", "Erro ao cadastrar cliente!")

    def delete(self):
        database = Database()

        try:
            database.cursor.execute("DELETE FROM client WHERE id = '" + self.id + "'")
            database.connection.commit()
            database.connection.close()

            return messagebox.showinfo("", "Cliente excluído com sucesso!")

        except:
            return messagebox.showwarning("", "Erro ao excluir cliente!")

    def update(self):
        database = Database()

        try:
            database.cursor.execute(
                "UPDATE client SET id = '" + self.id + "', name = '" + self.name + "', cpf = '" + self.cpf + "', birthdate = '" + self.birthdate + "', gender = '" + self.gender + "', city = '" + self.city + "' WHERE id = '" + self.id + "'")
            database.connection.commit()
            database.connection.close()

            return messagebox.showinfo("", "Cliente atualizado com sucesso!")

        except:
            return messagebox.showwarning("", "Erro ao atualizar cliente!")

    def select(self, client_id):
        database = Database()

        try:
            database.cursor.execute("SELECT * FROM client WHERE id = '" + client_id + "'")
            database.connection.commit()
            database.connection.close()

            data = []

            for row in data:
                self.id = row[0]
                self.name = row[1]
                self.cpf = row[2]
                self.birthdate = row[3]
                self.gender = row[4]
                self.city = row[5]

            return messagebox.showinfo("", "Busca feita com sucesso!")

        except:
            return messagebox.showwarning("","Erro ao buscar cliente!")
