from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

import subprocess, sys, platform
import os

from PIL import Image

from customtkinter import CTkLabel, CTkEntry, CTkButton, CTkFrame, CTkToplevel, CTk, CTkImage

from tkinter.ttk import Treeview
from tkinter.constants import END

from user.usercrud import UserCrud
from user.usertreeview import fetch, populate_treeview


class UserApp(CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("1200x520")
        self.title("CRUD    |     Usuários")

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..")
        self.pdf_icon = CTkImage(light_image=Image.open(os.path.join(image_path, "pdf_icon.png")),
                                 dark_image=Image.open(os.path.join(image_path, "pdf_icon.png")), size=(50, 50))

        # title
        self.title_entry = CTkLabel(self, text="")
        self.title_entry.place(relx=0.495, rely=0, anchor="n")


        # id, combobox, search_button (why i created a frame)
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
        self.password_entry = CTkEntry(self, placeholder_text="Senha", show="•")
        self.password_entry.place(relx=0.5, rely=0.4, anchor="n")


        # buttons (insert, update, delete, search_id)
        """
        self.search_button = CTkButton(self.id_frame, text="Buscar ID", width=80, command=self.select)
        self.search_button.place(relx=0.74, rely=0.5, anchor="center")
        """

        self.button_frame = CTkFrame(self, width=300, height=50, fg_color="transparent")
        self.delete_button = CTkButton(self.button_frame, text="Excluir", width=80, command=self.delete)
        self.update_button = CTkButton(self.button_frame, text="Atualizar", width=80, command=self.update)
        self.insert_button = CTkButton(self.button_frame, text="Inserir", width=80, command=self.insert)

        self.button_frame.place(relx=0.52, rely=0.47, anchor="n")
        self.delete_button.place(relx=0, rely=0.25)
        self.update_button.place(relx=0.3, rely=0.25)
        self.insert_button.place(relx=0.6, rely=0.25)
        
        # pdf button (top right)
        self.pdf_button = CTkButton(self, width=0, height=0, fg_color="transparent", image=self.pdf_icon, text="",
                                    command=self.pdf)
        self.pdf_button.place(relx=0.96, rely=0.02, anchor="n")


        # treeview
        self.treeview = Treeview(self, columns=("id", "name", "phone", "email", "username", "password"), show="headings")

        self.treeview.heading("id", text="ID")
        self.treeview.heading("name", text="NOME")
        self.treeview.heading("phone", text="TELEFONE")
        self.treeview.heading("email", text="EMAIL")
        self.treeview.heading("username", text="USERNAME")
        self.treeview.heading("password", text="SENHA")

        fetch()
        populate_treeview(self.treeview)
        self.treeview.bind("<<TreeviewSelect>>", self.synchronize)
        self.treeview.place(relx=0.5, rely=0.6, anchor="n")

    # crud methods
    def insert(self):
        user = UserCrud(self.id_entry.get(), self.name_entry.get(), self.phone_entry.get(), self.email_entry.get(), self.username_entry.get(), self.password_entry.get()) 
        
        user.insert()
        
        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END) 
    
    
    def update(self):
        user = UserCrud(self.id_entry.get(), self.name_entry.get(), self.phone_entry.get(), self.email_entry.get(), self.username_entry.get(), self.password_entry.get()) 
        
        user.update()
        
        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END) 
    
    
    def delete(self):
        user = UserCrud(self.id_entry.get(), self.name_entry.get(), self.phone_entry.get(), self.email_entry.get(), self.username_entry.get(), self.password_entry.get()) 
        
        user.delete()
        
        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END) 
    
    """
    def select(self):
        user = UserCrud(self.id_entry.get(), self.name_entry.get(), self.phone_entry.get(), self.email_entry.get(), self.username_entry.get(), self.password_entry.get())

        user.select(self.id_entry.get())

        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
    """

    # treeview-row & window-entry synchronization
    def synchronize(self, event=None):
        for item in self.treeview.selection():
            values: [] = self.treeview.item(item, "values")

            self.id_entry.delete(0, END)
            self.id_entry.insert(0, values[0])

            self.name_entry.delete(0, END)
            self.name_entry.insert(0, values[1])

            self.phone_entry.delete(0, END)
            self.phone_entry.insert(0, values[2])

            self.email_entry.delete(0, END)
            self.email_entry.insert(0, values[3])

            self.username_entry.delete(0, END)
            self.username_entry.insert(0, values[4])

            self.password_entry.delete(0, END)
            self.password_entry.insert(0, values[5])

    def pdf(self):
        c = canvas.Canvas("../../exports/export_usuario.pdf", pagesize=letter)
        file_path = "../../exports/export_usuario.pdf"

        width, height = letter
        c.setFont("Helvetica", 10)

        x = 100
        y = height - 50

        c.drawString(x, y, "ID")
        c.drawString(x + 50, y, "NOME")
        c.drawString(x + 150, y, "TELEFONE")
        c.drawString(x + 230, y, "EMAIL")
        c.drawString(x + 350, y, "USERNAME")
        c.drawString(x + 450, y, "SENHA")

        y -= 20

        for row in fetch():
            c.drawString(x, y, str(row[0]))
            c.drawString(x + 50, y, str(row[1]))
            c.drawString(x + 150, y, str(row[2]))
            c.drawString(x + 230, y, str(row[3]))
            c.drawString(x + 350, y, str(row[4]))
            c.drawString(x + 450, y, str(row[5]))

            y -= 15

            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 10)
                y = height - 50
                c.drawString(x, y, "ID")
                c.drawString(x + 50, y, "NOME")
                c.drawString(x + 150, y, "TELEFONE")
                c.drawString(x + 230, y, "EMAIL")
                c.drawString(x + 350, y, "USERNAME")
                c.drawString(x + 450, y, "SENHA")

                y -= 20

        c.save()

        if platform.system() == "Windows":
            os.startfile(file_path)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"  # linux
            subprocess.call([opener, file_path])












