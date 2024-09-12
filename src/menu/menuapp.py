from os import path
from PIL import Image
from customtkinter import CTkImage, CTk, CTkFrame, CTkLabel, CTkButton, CTkFont, CTkOptionMenu, \
    set_appearance_mode

from city.cityapp import CityApp
from client.clientapp import ClientApp
from user.userapp import UserApp


class MenuApp(CTk):
    def __init__(self):
        super().__init__()

        self.title("")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = path.join(path.dirname(path.realpath(__file__)), ".")

        self.logo_image = CTkImage(Image.open(path.join(image_path, "icon.ico")), size=(27, 27))
        self.user_icon = CTkImage(light_image=Image.open(path.join(image_path, "user_icon.png")),
                                  dark_image=Image.open(path.join(image_path, "user_icon.png")), size=(20, 20))
        self.client_icon = CTkImage(light_image=Image.open(path.join(image_path, "client_icon.png")),
                                    dark_image=Image.open(path.join(image_path, "client_icon.png")), size=(20, 20))
        self.city_icon = CTkImage(light_image=Image.open(path.join(image_path, "city_icon.png")),
                                  dark_image=Image.open(path.join(image_path, "city_icon.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = CTkLabel(self.navigation_frame, text="  CRUD", image=self.logo_image,
                                               compound="left", font=CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.user_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                     text="Usuário",
                                     fg_color="transparent", text_color=("gray10", "gray90"),
                                     hover_color=("gray70", "gray30"),
                                     image=self.user_icon, anchor="w", command=self.user_button_event)
        self.user_button.grid(row=1, column=0, sticky="ew")

        self.client_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                       text="Cliente",
                                       fg_color="transparent", text_color=("gray10", "gray90"),
                                       hover_color=("gray70", "gray30"),
                                       image=self.client_icon, anchor="w", command=self.client_button_event)
        self.client_button.grid(row=2, column=0, sticky="ew")

        self.city_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                     text="Cidade",
                                     fg_color="transparent", text_color=("gray10", "gray90"),
                                     hover_color=("gray70", "gray30"),
                                     image=self.city_icon, anchor="w", command=self.city_button_event)
        self.city_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                  command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")
        self.appearance_mode_menu.set("Tema")

        # content
        self.content_frame = CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.content_frame.grid_columnconfigure(0, weight=1)

        self.toplevel_window = None

    def user_button_event(self):
        self.toplevel_window = UserApp()

    def client_button_event(self):
        self.toplevel_window = ClientApp()

    def city_button_event(self):
        self.toplevel_window = CityApp()


    def change_appearance_mode_event(self, new_appearance_mode):
        set_appearance_mode(new_appearance_mode)


window = MenuApp()
window.mainloop()
