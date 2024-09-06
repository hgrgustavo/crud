from customtkinter import CTk, CTkLabel, CTkFrame, CTkEntry, CTkOptionMenu

from tkinter.ttk import Treeview


class ClientApp(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x530")
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

        # city_id
        self.cityid_frame = CTkFrame(self, border_color="orange", border_width=1,width=80, height=30, fg_color="orange3", corner_radius=6)
        self.cityid_label = CTkLabel(self.cityid_frame, text="ID Cidade")
        self.cityid_frame.place(relx=0.4999, rely=0.41, anchor="n")
        self.cityid_label.place(relx=0.5, rely=0.08, anchor="n")


        # treeview
        self.treeview = Treeview(self, columns=("id", "name", "cpf", "gender", "cityid"), show="headings", height=100)

        self.treeview.heading("id", text="ID")
        self.treeview.heading("name", text="NOME")
        self.treeview.heading("cpf", text="CPF / CNPJ")
        self.treeview.heading("gender", text="GÊNERO")
        self.treeview.heading("cityid", text="ID CIDADE")

        self.treeview.place(relx=0.5, rely=0.55, anchor="n")

        # crud methods







window = ClientApp()
window.mainloop()