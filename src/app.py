"""
        Login Missing Features

    ~ Auth button (login >>> auth >>> Menu)
    ~ Forget password (login >>> entry new password form)
    ~ Create new account (login >>> New user form)

    User Missing Features

    ~ Choose between CPF our CNPJ

    General Missing Features

    ~ When press a button, a blue line cross the window on x axis, like Google Chrome

"""

from customtkinter import CTk, CTkImage, CTkFrame, CTkLabel, CTkFont, CTkEntry, CTkButton, CTkToplevel, CTkOptionMenu
# from tkinter.ttk import Separator
from os import path
from PIL import Image
from treeview import UserTreeview, ClientTreeview, CityTreeview


# icons path
icons_path = path.join(path.dirname(path.realpath(__file__)), "icons/")


class Login(CTk):
    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry("1000x550")

        """
        self.separator = Separator(self, orient="vertical")
        self.separator.place(relx=0.5, rely=0.1, height=450)
        """

        # loading logo icon inside a container
        self.logo_icon = CTkImage(Image.open(path.join(icons_path, "logo_icon.png")), size=(70, 70))


        # left-frame (phrase below logo)
        self.left_frame = CTkFrame(self, width=501, height=451, fg_color="transparent")
        self.left_frame.place(relx=0.23, rely=0.1, anchor="n")

        self.logo_label = CTkLabel(self.left_frame, image=self.logo_icon, text="\tCRUD", font=CTkFont(size=40, weight="bold"))
        self.logo_label.place(relx=0.126, rely=0.22)

        self.phrase_label = CTkLabel(self.left_frame,
                                     text="            CRUD ajuda você a armazenar e \n    gerir informações de forma\ndinâmica.\t        ",
                                     font=CTkFont(size=20, weight="bold"))
        self.phrase_label.place(relx=0.217, rely=0.41)


        # right-frame (card-style form)
        self.right_frame = CTkFrame(self, width=347, height=350, fg_color="white")
        self.right_frame.place(relx=0.69, rely=0.13, anchor="n")

        self.email_entry = CTkEntry(self.right_frame, placeholder_text="Email ou telefone", width=315, height=50,
                                    fg_color="white", text_color="black", border_width=1, border_color="#dadde1")
        self.password_entry = CTkEntry(self.right_frame, placeholder_text="Senha", width=315, height=50,
                                       fg_color="white", text_color="black", show="•", border_width=1,
                                       border_color="#dadde1")
        self.email_entry.place(relx=0.5, rely=0.05, anchor="n")
        self.password_entry.place(relx=0.5, rely=0.214, anchor="n")

        self.login_button = CTkButton(self.right_frame, fg_color="#0836FF", text_color="white", text="Entrar",
                                      font=CTkFont(size=15, weight="bold"), width=315, height=45, hover=False) # command=self.auth)
        self.login_button.place(relx=0.5, rely=0.4, anchor="n")

        self.forget_password = CTkLabel(self.right_frame, text="Esqueceu a senha?", text_color="#0836FF")
        self.forget_password.place(relx=0.5, rely=0.565, anchor="n")

        self.container_separator = CTkFrame(self.right_frame, bg_color="#dadde1", width=315, height=1)
        self.container_separator.place(relx=0.5, rely=0.7, anchor="n")

        self.new_account_button = CTkButton(self.right_frame, fg_color="#30b000", text_color="white",
                                            text="Criar nova conta", font=CTkFont(size=14, weight="bold"), width=160,
                                            height=44, hover=False)
        self.new_account_button.place(relx=0.5, rely=0.777, anchor="n")


class Menu(CTk):
    def __init__(self):
        super().__init__()
        self.title("CRUD     |      Login")
        self.geometry("1000x575")

        # loading menu icons
        self.logo_icon = CTkImage(Image.open(path.join(icons_path, "logo_icon.png")), size=(50, 50))
        self.user_icon = CTkImage(light_image=Image.open(path.join(icons_path, "user_icon.png")), dark_image=Image.open(path.join(icons_path, "user_icon.png")), size=(30, 30))
        self.client_icon = CTkImage(light_image=Image.open(path.join(icons_path, "client_icon.png")), dark_image=Image.open(path.join(icons_path, "client_icon.png")), size=(30, 30))
        self.city_icon = CTkImage(light_image=Image.open(path.join(icons_path, "city_icon.png")), dark_image=Image.open(path.join(icons_path, "city_icon.png")), size=(30, 30))

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # nav
        self.nav_frame = CTkFrame(self, corner_radius=0)
        self.nav_frame.grid(row=0, column=0, sticky="nsew")

        self.nav_label = CTkLabel(self.nav_frame, text=" CRUD", image=self.logo_icon, compound="left", font=CTkFont(size=25, weight="bold"))
        self.nav_label.grid(row=0, column=0, padx=20, pady=20)

        """
        test inserting a separator between logo and cruds
        
        """

        self.user_button = CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10, text="Usuário", fg_color="transparent", text_color=("gray10", "gray70"), hover_color=("gray70", "gray30"), image=self.user_icon, anchor="w")
        # command=self.open_userwindow)
        self.user_button.grid(row=1, column=0, sticky="ew")

        self.client_button = CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10, text="Cliente", fg_color="transparent", text_color=("gray10", "gray70"), hover_color=("gray70", "gray30"), image=self.client_icon, anchor="w")
        # command=self.open_clientwindow
        self.client_button.grid(row=2, column=0, stick="ew")

        self.city_button = CTkButton(self.nav_frame, corner_radius=0, height=40, border_spacing=10, text="Cidade", fg_color="transparent", text_color=("gray10", "gray70"), hover_color=("gray70", "gray30"), image=self.city_icon, anchor="w")
        # command-self.open_citywindow
        self.city_button.grid(row=3, column=0, sticky="ew")

        self.theme_menu = CTkOptionMenu(self.nav_frame, values=["Light", "Dark", "System"])
        self.theme_menu.set("Tema")
        # command=self.change_theme)
        self.theme_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # content
        self.content_frame = CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.content_frame.grid_columnconfigure(0, weight=1)

    # callback methods



# loading pdf icon
pdf_icon = CTkImage(light_image=Image.open(path.join(icons_path, "pdf_icon.png")), dark_image=Image.open(path.join(icons_path, "pdf_icon.png")), size=(60, 60))


class User(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x520")
        self.title("CRUD    |    Usuários")

        # entries
        self.entries_frame = CTkFrame(self, width=400, height=280, fg_color="transparent")
        self.entries_frame.place(relx=0.5, rely=0.00, anchor="n")

        self.id_entry = CTkEntry(self.entries_frame, placeholder_text="Identificador")
        self.id_entry.place(relx=0.32, rely=0.065)

        self.name_entry = CTkEntry(self.entries_frame, placeholder_text="Nome completo")
        self.name_entry.place(relx=0.32, rely=0.187)

        self.phone_entry = CTkEntry(self.entries_frame, placeholder_text="Nº Telefone")
        self.phone_entry.place(relx=0.32, rely=0.308)

        self.email_entry = CTkEntry(self.entries_frame, placeholder_text="Email")
        self.email_entry.place(relx=0.32, rely=0.43)

        self.username_entry = CTkEntry(self.entries_frame, placeholder_text="Username")
        self.username_entry.place(relx=0.32, rely=0.55)

        self.password_entry = CTkEntry(self.entries_frame, placeholder_text="Senha")
        self.password_entry.place(relx=0.32, rely=0.67)

        # crud buttons
        self.insert_button = CTkButton(self.entries_frame, text="INSERT", width=96, height=39) # command=self.)
        self.insert_button.place(relx=0.22, rely=0.85, anchor="n")

        self.update_button = CTkButton(self.entries_frame, text="UPDATE", width=96, height=39) # command=self.)
        self.update_button.place(relx=0.48, rely=0.85, anchor="n")

        self.delete_button = CTkButton(self.entries_frame, text="DELETE", width=96, height=39) # command=self.)
        self.delete_button.place(relx=0.74, rely=0.85, anchor="n")

        # pdf button
        self.pdf_button = CTkButton(self, text="", image=pdf_icon, fg_color="transparent", width=0, height=0)
        self.pdf_button.place(relx=0.02, rely=0.07, anchor="w")

        # treeview
        self.user_treeview = UserTreeview()


class Client(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x520")
        self.title("CRUD    |    Cliente")

        # entries
        self.entries_frame = CTkFrame(self, width=400, height=280, fg_color="transparent")
        self.entries_frame.place(relx=0.5, rely=0.00, anchor="n")

        self.id_entry = CTkEntry(self.entries_frame, placeholder_text="Identificador")
        self.id_entry.place(relx=0.32, rely=0.065)

        self.name_entry = CTkEntry(self.entries_frame, placeholder_text="Nome completo")
        self.name_entry.place(relx=0.32, rely=0.187)

        self.cpf_entry = CTkEntry(self.entries_frame, placeholder_text="CPF" )
        self.cpf_entry.place(relx=0.32, rely=0.308)

        self.cnpj_entry = CTkEntry(self.entries_frame, placeholder_text="CNPJ" )
        self.cnpj_entry.place(relx=0.32, rely=0.43)

        """
        O seu cliente é uma pessoa ou uma empress?
        
        [ ] - Pessoa        [X] - Empresa ou MEI
        
        >> Se for empresa, bloquear entry do CPF
        >> else bloquear entry CNPJ
        """

        # crud buttons
        self.insert_button = CTkButton(self.entries_frame, text="INSERT", width=96, height=39) # command=self.)
        self.insert_button.place(relx=0.22, rely=0.6, anchor="n")

        self.update_button = CTkButton(self.entries_frame, text="UPDATE", width=96, height=39) # command=self.)
        self.update_button.place(relx=0.48, rely=0.6, anchor="n")

        self.delete_button = CTkButton(self.entries_frame, text="DELETE", width=96, height=39) # command=self.)
        self.delete_button.place(relx=0.74, rely=0.6, anchor="n")

        # pdf button
        self.pdf_button = CTkButton(self, text="", image=pdf_icon, fg_color="transparent", width=0, height=0)
        self.pdf_button.place(relx=0.02, rely=0.07, anchor="w")

        # treeview
        self.user_treeview = ClientTreeview()

class City(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x520")
        self.title("CRUD    |    Cidade")

        # entries
        self.entries_frame = CTkFrame(self, width=400, height=280, fg_color="transparent")
        self.entries_frame.place(relx=0.5, rely=0.00, anchor="n")

        self.id_entry = CTkEntry(self.entries_frame, placeholder_text="Identificador")
        self.id_entry.place(relx=0.32, rely=0.065)

        self.name_entry = CTkEntry(self.entries_frame, placeholder_text="Cidade")
        self.name_entry.place(relx=0.32, rely=0.187)

        self.cpf_entry = CTkEntry(self.entries_frame, placeholder_text="Estado" )
        self.cpf_entry.place(relx=0.32, rely=0.308)

        self.cnpj_entry = CTkEntry(self.entries_frame, placeholder_text="País" )
        self.cnpj_entry.place(relx=0.32, rely=0.43)

        # crud buttons
        self.insert_button = CTkButton(self.entries_frame, text="INSERT", width=96, height=39) # command=self.)
        self.insert_button.place(relx=0.22, rely=0.6, anchor="n")

        self.update_button = CTkButton(self.entries_frame, text="UPDATE", width=96, height=39) # command=self.)
        self.update_button.place(relx=0.48, rely=0.6, anchor="n")

        self.delete_button = CTkButton(self.entries_frame, text="DELETE", width=96, height=39) # command=self.)
        self.delete_button.place(relx=0.74, rely=0.6, anchor="n")

        # pdf button
        self.pdf_button = CTkButton(self, text="", image=pdf_icon, fg_color="transparent", width=0, height=0)
        self.pdf_button.place(relx=0.02, rely=0.07, anchor="w")

        # treeview
        self.user_treeview = CityTreeview()



window = Menu()
window.mainloop()



       
        
    



