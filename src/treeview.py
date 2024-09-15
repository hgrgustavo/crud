from tkinter.ttk import Treeview


class UserTreeview(Treeview):
    def __init__(self):
        super().__init__(columns=("id", "name", "phone", "email", "username", "password"), show="headings", height=12)

        # defining headings
        self.heading("id", text="ID")
        self.heading("name", text="NOME")
        self.heading("phone", text="TELEFONE")
        self.heading("email", text="EMAIL")
        self.heading("username", text="USERNAME")
        self.heading("password", text="SENHA")


        self.pack(fill="x", side="bottom", pady=0)