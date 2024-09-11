import os
from PIL import Image
from customtkinter import CTkImage, CTk, CTkFrame, CTkLabel, CTkButton, CTkFont, CTkOptionMenu, \
    set_appearance_mode

from city.cityapp import CityApp
from client.clientapp import ClientApp
from user.userapp import UserApp


class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("image_example.py")
        self.geometry("700x450")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), ".")
        self.logo_image = CTkImage(Image.open(os.path.join(image_path, "icon.ico")), size=(26, 26))
        self.large_test_image = CTkImage(Image.open(os.path.join(image_path, "client_icon.png")), size=(500, 150))
        self.image_icon_image = CTkImage(Image.open(os.path.join(image_path, "client_icon.png")), size=(20, 20))
        self.home_image = CTkImage(light_image=Image.open(os.path.join(image_path, "user_icon.png")),
                                   dark_image=Image.open(os.path.join(image_path, "user_icon.png")), size=(20, 20))
        self.chat_image = CTkImage(light_image=Image.open(os.path.join(image_path, "client_icon.png")),
                                   dark_image=Image.open(os.path.join(image_path, "client_icon.png")), size=(20, 20))
        self.add_user_image = CTkImage(light_image=Image.open(os.path.join(image_path, "city_icon.png")),
                                       dark_image=Image.open(os.path.join(image_path, "city_icon.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = CTkLabel(self.navigation_frame, text="  CRUD", image=self.logo_image,
                                               compound="left", font=CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                     text="Usuário",
                                     fg_color="transparent", text_color=("gray10", "gray90"),
                                     hover_color=("gray70", "gray30"),
                                     image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                        text="Cliente",
                                        fg_color="transparent", text_color=("gray10", "gray90"),
                                        hover_color=("gray70", "gray30"),
                                        image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                        text="Cidade",
                                        fg_color="transparent", text_color=("gray10", "gray90"),
                                        hover_color=("gray70", "gray30"),
                                        image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                  command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # content
        self.content_frame = CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.content_frame.grid_columnconfigure(0, weight=1)

        self.toplevel_window = None
        """
        self.content_frame_large_image_label = CTkLabel(self.content_frame, text="", image=self.large_test_image)
        self.content_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
        """

    def home_button_event(self):
        self.toplevel_window = UserApp()  # create window if its None or destroyed

    def frame_2_button_event(self):
        self.toplevel_window = ClientApp()  # create window if its None or destroyed

    def frame_3_button_event(self):
        self.toplevel_window = CityApp()  # create window if its None or destroyed

    def change_appearance_mode_event(self, new_appearance_mode):
        set_appearance_mode(new_appearance_mode)


app = App()
app.mainloop()
