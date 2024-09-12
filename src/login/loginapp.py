from os import path
from PIL import Image
from customtkinter import CTk, CTkImage, CTkLabel, CTkFont, CTkFrame
from tkinter.ttk import Separator

class LoginApp(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x650")

        # separator
        self.separator = Separator(self, orient="vertical")
        self.separator.place(relx=0.5, rely=0.1, height=450)


        # left-side
        self.path = path.join(path.dirname(path.realpath(__file__)), "../menu")
        self.logo_icon = CTkImage(Image.open(path.join(self.path, "icon.ico")), size=(50, 50))

        self.left_frame = CTkFrame(self, width=340, height=400, fg_color="transparent")
        self.left_frame.place(relx=0.15, rely=0.1)

        self.logo_label = CTkLabel(self.left_frame, text="\tCRUD", image=self.logo_icon, font=CTkFont(size=30, weight="bold"))
        self.logo_label.place(relx=0, rely=0.3)

        self.phrase_label = CTkLabel(self.left_frame, text="            CRUD ajuda você a armazenar e\n     gerir informações de forma \ndinâmica.", font=CTkFont(size=14, weight="bold"))
        self.phrase_label.place(relx=0.1, rely=0.44)

        # right-side








