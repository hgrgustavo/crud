from tkinter.ttk import Treeview


class UserTreeview(Treeview):
    def __init__(self):
        super().__init__(columns=("id", "name", "phone", "email", "username", "password"), show="headings", height=10)

        # defining headings
        self.heading("id", text="ID")
        self.heading("name", text="NOME")
        self.heading("phone", text="TELEFONE")
        self.heading("email", text="EMAIL")
        self.heading("username", text="USERNAME")
        self.heading("password", text="SENHA")

        self.pack(fill="x", side="bottom")



class ClientTreeview(Treeview):
    def __init__(self):
        super().__init__(columns=("id", "name", "cpf", "cnpj"), show="headings", height=10)

        # defining headings
        self.heading("id", text="ID")
        self.heading("name", text="NOME")
        self.heading("cpf", text="CPF")
        self.heading("cnpj", text="CNPJ")

        self.pack(fill="x", side="bottom")



class CityTreeview(Treeview):
    def __init__(self):
        super().__init__(columns=("id", "city", "state", "country"), show="headings", height=10)

        # defining headings
        self.heading("id", text="ID")
        self.heading("city", text="CIDADE")
        self.heading("state", text="ESTADO")
        self.heading("country", text="PAÍS")

        self.pack(fill="x", side="bottom")