from os import path
from PIL import Image

from customtkinter import CTk, CTkImage, CTkLabel, CTkFont, CTkFrame, CTkEntry, CTkButton
from tkinter import messagebox

from menu.menuapp import MenuApp
from database import Database


# from tkinter.ttk import Separator

class LoginApp(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x650")
        self.title("CRUD    |     Login")


        """
        # separator
        self.separator = Separator(self, orient="vertical")
        self.separator.place(relx=0.5, rely=0.1, height=450)
        """

        # left-side
        self.path = path.join(path.dirname(path.realpath(__file__)), "../menu")
        self.logo_icon = CTkImage(Image.open(path.join(self.path, "logo_icon.png")), size=(55, 50))

        self.left_frame = CTkFrame(self, width=340, height=400, fg_color="transparent")
        self.left_frame.place(relx=0.22, rely=0.1)

        self.logo_label = CTkLabel(self.left_frame, text="\t CRUD", image=self.logo_icon, font=CTkFont(size=30, weight="bold"))
        self.logo_label.place(relx=0, rely=0.3)

        self.phrase_label = CTkLabel(self.left_frame, text="            CRUD ajuda você a armazenar e\n    gerir informações de forma\ndinâmica.", font=CTkFont(size=14, weight="bold"))
        self.phrase_label.place(relx=0.12, rely=0.47)

        # right-side
        self.right_frame = CTkFrame(self, fg_color="white", width=347, height=350)
        self.right_frame.place(relx=0.55, rely=0.15)

        self.email_entry = CTkEntry(self.right_frame, placeholder_text="Email ou telefone", width=315, height=50, fg_color="white", text_color="black", border_width=1, border_color="#dadde1")
        self.password_entry = CTkEntry(self.right_frame, placeholder_text="Senha", width=315, height=50, fg_color="white", text_color="black", show="•", border_width=1, border_color="#dadde1")
        self.email_entry.place(relx=0.5, rely=0.05, anchor="n")
        self.password_entry.place(relx=0.5, rely=0.214, anchor="n")

        self.login_button = CTkButton(self.right_frame, fg_color="#0836FF", text_color="white", text="Entrar", font=CTkFont(size=15, weight="bold"), width=315, height=45, command=self.auth)
        self.login_button.place(relx=0.5, rely=0.4, anchor="n")

        self.forget_password = CTkLabel(self.right_frame, text="Esqueceu a senha?", text_color="#0836FF")
        self.forget_password.place(relx=0.5, rely=0.565, anchor="n")

        self.container_separator = CTkFrame(self.right_frame, bg_color="#dadde1", width=315, height=1)
        self.container_separator.place(relx=0.5, rely=0.7, anchor="n")

        self.new_account_button = CTkButton(self.right_frame, fg_color="#30b000", text_color="white", text="Criar nova conta", font=CTkFont(size=14, weight="bold"), width=160, height=44)
        self.new_account_button.place(relx=0.5, rely=0.777, anchor="n")

    def auth(self):
        database = Database()

        self.open_menu() if database.cursor.execute("SELECT email, phone, password FROM user WHERE email = ? OR phone = ? AND password = ?", (self.email_entry.get(), self.email_entry.get(), self.password_entry.get())).fetchone() else messagebox.showerror("", "Credênciais inválidas :(")

    def open_menu(self):
        messagebox.showinfo("", "Você esta autenticado! Bem vindo :)")

        self.destroy()
        MenuApp()


window = LoginApp()
window.mainloop()








