from tkinter import messagebox
from database import Database


class UserCrud:
    def __init(self, client_id, name: str, cpf: str, birthdate: str, gender: str, city_id):
        self.id = client_id
        self.name = name
        self.cpf = cpf
        self.birthdate = birthdate
        self.gender = gender

        self.city_id = city_id  # foreign key


    def insert(self) -> messagebox:
        database = Database()

        try:
            database.cursor.execute("insert into client (name, cpf, birthdate, gender")


