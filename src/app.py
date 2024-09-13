"""
        Login Missing Setup

    ~ Auth button (login >>> Menu)
    ~ Forget password (login >>> entry new password form)
    ~ Create new account (login >>> New user form)

"""

from customtkinter import CTk, CTkImage, CTkFrame, CTkLabel, CTkFont, CTkEntry, CTkButton

# from tkinter.ttk import Separator

from os import path
from PIL import Image

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
                                      font=CTkFont(size=15, weight="bold"), width=315, height=45) # command=self.auth)
        self.login_button.place(relx=0.5, rely=0.4, anchor="n")

        self.forget_password = CTkLabel(self.right_frame, text="Esqueceu a senha?", text_color="#0836FF")
        self.forget_password.place(relx=0.5, rely=0.565, anchor="n")

        self.container_separator = CTkFrame(self.right_frame, bg_color="#dadde1", width=315, height=1)
        self.container_separator.place(relx=0.5, rely=0.7, anchor="n")

        self.new_account_button = CTkButton(self.right_frame, fg_color="#30b000", text_color="white",
                                            text="Criar nova conta", font=CTkFont(size=14, weight="bold"), width=160,
                                            height=44)
        self.new_account_button.place(relx=0.5, rely=0.777, anchor="n")


class Menu:

