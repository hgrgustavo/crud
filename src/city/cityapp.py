import platform

from customtkinter import CTk, CTkLabel, CTkEntry, CTkFrame, CTkButton, CTkToplevel, CTkImage

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

import subprocess, sys, os

from PIL import Image

from tkinter.ttk import Treeview
from tkinter.constants import END

from city.citycrud import CityCrud
from city.citytreeview import fetch, populate_treeview


class CityApp(CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("CRUD    |     Cidades")
        self.geometry("800x446")

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
        self.pdf_icon = CTkImage(light_image=Image.open(os.path.join(image_path, "pdf_icon.png")),
                                  dark_image=Image.open(os.path.join(image_path, "pdf_icon.png")), size=(50, 50))

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

        # pdf button (top right)
        self.pdf_button = CTkButton(self, width=0, height=0, fg_color="transparent", image=self.pdf_icon, text="", command=self.pdf)
        self.pdf_button.place(relx=0.96, rely=0.02, anchor="n")


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

    def pdf(self):
        c = canvas.Canvas("../../exports/export_cidade.pdf", pagesize=letter)
        file_path = "../../exports/export_cidade.pdf"

        width, height = letter
        c.setFont("Helvetica", 10)

        x = 100
        y = height - 50

        c.drawString(x, y, "ID")
        c.drawString(x + 50, y, "CIDADE")
        c.drawString(x + 150, y, "ESTADO")
        c.drawString(x + 230, y, "PAÍS")
      

        y -= 20

        for row in fetch():
            c.drawString(x, y, str(row[0]))
            c.drawString(x + 50, y, str(row[1]))
            c.drawString(x + 150, y, str(row[2]))
            c.drawString(x + 230, y, str(row[3]))
          
            y -= 15

            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 10)
                y = height - 50
                c.drawString(x, y, "ID")
                c.drawString(x + 50, y, "CIDADE")
                c.drawString(x + 150, y, "ESTADO")
                c.drawString(x + 230, y, "PAÍS")

                y -= 20

        c.save()


        if platform.system() == "Windows":
            os.startfile(file_path)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"     # linux
            subprocess.call([opener, file_path])








