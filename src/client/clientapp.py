from customtkinter import CTk, CTkLabel, CTkFrame, CTkEntry, CTkOptionMenu, CTkComboBox, CTkButton

from tkinter.ttk import Treeview
from tkinter.constants import END

from clientcombobox import get_cityname
from clientcrud import ClientCrud
from clientreeview import fetch, populate_treeview



class ClientApp(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x550")
        self.title("Cadastro  |  Cliente")

        # title
        self.title_entry = CTkLabel(self, text="")
        self.title_entry.place(relx=0.495, rely=0, anchor="n")

        # id, search_button (why i created a frame)
        self.id_frame = CTkFrame(master=self, width=500, height=40, fg_color="transparent")
        self.id_entry = CTkEntry(self, placeholder_text="Identificador")

        self.id_frame.place(relx=0.5, rely=0.09, anchor="n")
        self.id_entry.place(relx=0.5, rely=0.1, anchor="n")

        # name
        self.name_entry = CTkEntry(self, placeholder_text="Nome completo")
        self.name_entry.place(relx=0.5, rely=0.16, anchor="n")

        # cpf or cnpj
        self.cpf_entry = CTkEntry(self, placeholder_text="CPF ou CNPJ")
        self.cpf_entry.place(relx=0.5, rely=0.22, anchor="n")

        # birthdate
        self.birthdate_entry = CTkEntry(self, placeholder_text="Data de nascimento")
        self.birthdate_entry.place(relx=0.5, rely=0.28, anchor="n")

        # gender
        self.gender_menu = CTkOptionMenu(self, values=["Masculino", "Feminino", "Outro"], hover=True)
        self.gender_menu.set("Gênero")
        self.gender_menu.place(relx=0.5, rely=0.34, anchor="n")

        # city combobox
        self.city_combobox = CTkComboBox(self)
        self.city_combobox.set("Cidade")

        get_cityname(self)

        self.city_combobox.place(relx=0.5, rely=0.40, anchor="n")

        # buttons (insert, update, delete, search_id)
        """
        self.search_button = CTkButton(self.id_frame, text="Buscar ID", width=80, command=self.select)
        self.search_button.place(relx=0.74, rely=0.5, anchor="center")
        """
        self.button_frame = CTkFrame(self, width=300, height=50, fg_color="transparent")
        self.delete_button = CTkButton(self.button_frame, text="Excluir", width=80, command=self.delete)
        self.update_button = CTkButton(self.button_frame, text="Atualizar", width=80, command=self.update)
        self.insert_button = CTkButton(self.button_frame, text="Inserir", width=80, command=self.insert)

        self.button_frame.place(relx=0.52, rely=0.46, anchor="n")
        self.delete_button.place(relx=0, rely=0.25)
        self.update_button.place(relx=0.3, rely=0.25)
        self.insert_button.place(relx=0.6, rely=0.25)

        # treeview
        self.treeview = Treeview(self, columns=("id", "name", "cpf", "birthdate", "gender", "city"), show="headings")

        self.treeview.heading("id", text="ID")
        self.treeview.heading("name", text="NOME")
        self.treeview.heading("cpf", text="CPF / CNPJ")
        self.treeview.heading("birthdate", text="DATA DE NASCIMENTO")
        self.treeview.heading("gender", text="GÊNERO")
        self.treeview.heading("city", text="CIDADE")

        fetch()
        populate_treeview(self.treeview)
        self.treeview.bind("<<TreeviewSelect>>", self.synchronize)

        self.treeview.place(relx=0.5, rely=0.6, anchor="n")


    # crud methods
    def insert(self):
        client = ClientCrud(self.id_entry.get(), self.name_entry.get(), self.cpf_entry.get(),
                            self.birthdate_entry.get(), self.gender_menu.get(), self.city_combobox.get())

        client.insert()

        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.birthdate_entry.delete(0, END)
        self.gender_menu.set("Gênero")
        self.city_combobox.set("Cidade")

    def update(self):
        client = ClientCrud(self.id_entry.get(), self.name_entry.get(), self.cpf_entry.get(),
                            self.birthdate_entry.get(), self.gender_menu.get(), self.city_combobox.get())

        client.update()

        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.birthdate_entry.delete(0, END)
        self.gender_menu.set("Gênero")
        self.city_combobox.set("Cidade")

    def delete(self):
        client = ClientCrud(self.id_entry.get(), self.name_entry.get(), self.cpf_entry.get(),
                            self.birthdate_entry.get(), self.gender_menu.get(), self.city_combobox.get())

        client.delete()

        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.birthdate_entry.delete(0, END)
        self.gender_menu.set("Gênero")
        self.city_combobox.set("Cidade")

    """
    def select(self):
        client = ClientCrud(self.id_entry.get(), self.name_entry.get(), self.cpf_entry.get(),
                            self.birthdate_entry.get(), self.gender_menu.get(), self.city_combobox.get())

        client.select(self.id_entry.get())

        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.birthdate_entry.delete(0, END)
        self.gender_menu.set("Gênero")
        self.city_combobox.set("Cidade")
    """

    # treeview-row & window-entry synchronization
    def synchronize(self, event=None):
        for item in self.treeview.selection():
            values: [] = self.treeview.item(item, "values")

            self.id_entry.delete(0, END)
            self.id_entry.insert(0, values[0])

            self.name_entry.delete(0, END)
            self.name_entry.insert(0, values[1])

            self.cpf_entry.delete(0,END)
            self.cpf_entry.insert(0, values[2])

            self.birthdate_entry.delete(0, END)
            self.birthdate_entry.insert(0, values[3])

            self.gender_menu.set(values[4])

            self.city_combobox.set(values[5])


window = ClientApp()
window.mainloop()
