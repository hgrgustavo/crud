from tkinter import messagebox
from database import Database


class UserCrud:
    def __init__(self, user_id, name: str, phone: str, email: str, username: str, password: str):
        self.id = user_id
        self.name = name
        self.phone = phone
        self.email = email
        self.username = username
        self.password = password


    def insert(self) -> messagebox:
        database = Database()

        try:
            database.cursor.execute("insert into user (name, phone, email, username, password) values ('" + self.name + "', '" + self.phone + "', '" + self.email + "', '" + self.username + "', '" + self.password + "')")
            database.connection.commit()
            database.connection.close()
            return messagebox.showinfo("", "Usuário cadastrado com sucesso!")
        
        except:
            return messagebox.showwarning("", "Erro ao cadastrar usuário!")


    def delete(self) -> messagebox:
        database = Database()

        try:
            database.cursor.execute("delete from user where id = '" + self.id + "'")
            database.connection.commit()
            database.connection.close()

            return messagebox.showinfo("", "Usuário excluído com sucesso!")

        except:
            return messagebox.showwarning("", "Erro ao excluir usuário!")


    def update(self) -> messagebox:
        database = Database()

        try:
            database.cursor.execute("update user set name = '" + self.name + "', phone = '" + self. phone + "', email = '" + self.email + "', username = '" + self.username + "', password = '" + self.password + "' where id = '" + self.id + "'")
            database.connection.commit()
            database.connection.close()

            return messagebox.showinfo("", "Usuário atualizado com sucesso!")

        except:
            return messagebox.showwarning("", "Erro ao atualizar usuário")


    def select(self, user_id) -> messagebox:
        database = Database()

        try:
            database.cursor.execute("select * from user where id = '" + user_id + "'")
            database.connection.commit()
            database.connection.close()

            data = []

            for row in data:
                self.id = row[0]
                self.name = row[1]
                self.phone = row[2]
                self.email = row[3]
                self.username = row[4]
                self.password = row[5]

            return messagebox.showinfo("", "Busca feita com sucesso!")

        except:
            return messagebox.showwarning("", "Erro ao buscar usuário")

#   def search_treeview(self) -> []:

