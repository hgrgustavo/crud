from customtkinter import CTk, CTkLabel, CTkEntry, CTkFrame, CTkButton, CTkToplevel

from tkinter.ttk import Treeview
from tkinter.constants import END

from city.citycrud import CityCrud
from city.citytreeview import fetch, populate_treeview


class CityApp(CTk):
    def __init__(self):
        super().__init__()
        self.title("CRUD    |     Cidades")
        self.geometry("800x446")

        # title
        self.title_entry = CTkLabel(self, text="")
        self.title_entry.place(relx=0.5, rely=0, anchor="n")

        # id
        self.id_entry = CTkEntry(self, placeholder_text="Identificador")
        self.id_entry.place(relx=0.5, rely=0.1, anchor="n")

        # name
        self.city_entry = CTkEntry(self, placeholder_text="Nome da cidade")
        self.city_entry.place(relx=0.5, rely=0.17, anchor="n")

        # state
        self.state_entry = CTkEntry(self, placeholder_text="Nome do estado")
        self.state_entry.place(relx=0.5, rely=0.24, anchor="n")

        # country
        self.country_entry = CTkEntry(self, placeholder_text="Nome do país")
        self.country_entry.place(relx=0.5, rely=0.309, anchor="n")

        # buttons (insert, update delete, search_id)
        """
        self.search_button = CTkButton(self.id_frame, text="Buscard ID", width=80, command=self.select_
        self.search_button.place(relx=0.73, rely=0.5, anchor="center")
        """

        self.button_frame = CTkFrame(self, width=300, height=50, fg_color="transparent")

        self.delete_button = CTkButton(self.button_frame, text="Exlcuir", width=80, command=self.delete)
        self.update_button = CTkButton(self.button_frame, text="Atualizar", width=80, command=self.update)
        self.insert_button = CTkButton(self.button_frame, text="Inserir", width=80, command=self.insert)

        self.button_frame.place(relx=0.52, rely=0.38, anchor="n")
        self.delete_button.place(relx=0, rely=0.24)
        self.update_button.place(relx=0.3, rely=0.24)
        self.insert_button.place(relx=0.6, rely=0.24)

        # treeview
        self.treeview = Treeview(self, columns=("id", "city", "state", "country"), show="headings")

        self.treeview.heading("id", text="ID")
        self.treeview.heading("city", text="CIDADE")
        self.treeview.heading("state", text="ESTADO")
        self.treeview.heading("country", text="PAÍS")

        fetch()
        populate_treeview(self.treeview)
        self.treeview.bind("<<TreeviewSelect>>", self.synchronize)

        self.treeview.place(relx=0.5, rely=0.55, anchor="n")

        # crud
    def delete(self):
        city = CityCrud(self.id_entry.get(), self.city_entry.get(), self.state_entry.get(), self.country_entry.get())

        city.delete()

        self.id_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.state_entry.delete(0, END)
        self.country_entry.delete(0, END)


    def update(self):
        city = CityCrud(self.id_entry.get(), self.city_entry.get(), self.state_entry.get(), self.country_entry.get())

        city.update()

        self.id_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.state_entry.delete(0, END)
        self.country_entry.delete(0, END)

    def insert(self):
        city = CityCrud(self.id_entry.get(), self.city_entry.get(), self.state_entry.get(), self.country_entry.get())

        city.insert()

        self.id_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.state_entry.delete(0, END)
        self.country_entry.delete(0, END)

    """
    def select(self):
        city = CityCrud(self.id_entry.get(), self.city_entry.get(), self.state_entry.get(), self.country_entry.get())

        city.select(self.id_entry.get())

        self.id_entry.delete(0, END)
        self.city_entry.delete(0, END)
        self.state_entry.delete(0, END)
        self.country_entry.delete(0, END)
    """

    # treeview-row & window-entry synchronization
    def synchronize(self, event=None):
        for item in self.treeview.selection():
            values: [] = self.treeview.item(item, "values")

            self.id_entry.delete(0, END)
            self.id_entry.insert(0, values[0])

            self.city_entry.delete(0, END)
            self.city_entry.insert(0, values[1])

            self.state_entry.delete(0, END)
            self.state_entry.insert(0, values[2])

            self.country_entry.delete(0, END)
            self.country_entry.insert(0, values[3])







