from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton, CTkFrame
from tkinter.ttk import Treeview

class UserApp(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x520")
        self.title("Cadastro   |   Usuário")

        # title
        self.title_entry = CTkLabel(self, text="")
        self.title_entry.place(relx=0.495, rely=0, anchor="n")


        # id, combobox, search_button
        self.id_frame = CTkFrame(master=self, width=500, height=40, fg_color="transparent")
        self.id_entry = CTkEntry(self, placeholder_text="Identificador")

        self.id_frame.place(relx=0.5, rely=0.09, anchor="n")
        self.id_entry.place(relx=0.5, rely=0.1, anchor="n")

        # name
        self.name_entry = CTkEntry(self, placeholder_text="Nome completo")
        self.name_entry.place(relx=0.5, rely=0.16, anchor="n")

        # phone
        self.phone_entry = CTkEntry(self, placeholder_text="Nº telefone")
        self.phone_entry.place(relx=0.5, rely=0.22, anchor="n")

        # email
        self.email_entry = CTkEntry(self, placeholder_text="Endereço de email")
        self.email_entry.place(relx=0.5, rely=0.28, anchor="n")

        # username
        self.username_entry = CTkEntry(self, placeholder_text="Nome de usuário")
        self.username_entry.place(relx=0.5, rely=0.34, anchor="n")

        # password
        self.password_entry = CTkEntry(self, placeholder_text="Senha")
        self.password_entry.place(relx=0.5, rely=0.4, anchor="n")


        # buttons (insert, update, delete, search_id)
        self.search_button = CTkButton(self.id_frame, text="Buscar ID", width=80)
        self.search_button.place(relx=0.74, rely=0.5, anchor="center")

        self.button_frame = CTkFrame(self, width=300, height=50, fg_color="transparent")

        self.delete_button = CTkButton(self.button_frame, text="Excluir", width=80)
        self.update_button = CTkButton(self.button_frame, text="Atualizar", width=80)
        self.insert_button = CTkButton(self.button_frame, text="Inserir", width=80)

        self.button_frame.place(relx=0.52, rely=0.47, anchor="n")
        self.delete_button.place(relx=0, rely=0.25)
        self.update_button.place(relx=0.3, rely=0.25)
        self.insert_button.place(relx=0.6, rely=0.25)

        # treeview
        self.treeview = Treeview(self, columns=("id", "name", "phone", "email", "username", "password"), show="headings")

        self.treeview.heading("id", text="ID")
        self.treeview.heading("name", text="NOME")
        self.treeview.heading("phone", text="TELEFONE")
        self.treeview.heading("email", text="EMAIL")
        self.treeview.heading("username", text="USERNAME")
        self.treeview.heading("password", text="SENHA")

        self.treeview.place(relx=0.5, rely=0.6, anchor="n")

        # crud methods

window = UserApp()
window.mainloop()


