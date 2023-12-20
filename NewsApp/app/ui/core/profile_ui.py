from tkinter import *
import customtkinter
from data.user_dao import UserDAO
from PIL import Image


print(Image.open("static/image/user.png").size)


class ProfileUI(customtkinter.CTkFrame):
    def __init__(self, master, app, currentUser):
        super().__init__(master)
        self.app = app
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        # User icons created by kmg design - Flaticon
        self.profile_image = customtkinter.CTkImage(
            light_image=Image.open("static/image/user.png"),
            dark_image=Image.open("static/image/user.png"),
            size=(64, 64))

        self.image_label = customtkinter.CTkLabel(
            master, image=self.profile_image, text="")
        self.image_label.grid(row=0, column=0, padx=20, pady=10)

        if currentUser is not None:
            # nome do usuário
            self.name = customtkinter.CTkLabel(
                master, text=currentUser.name)
            self.name.grid(row=1, column=0, padx=20, pady=10)

            # email do usuário
            self.email = customtkinter.CTkLabel(
                master, text=currentUser.email)
            self.email.grid(row=2, column=0, padx=20, pady=10)

            # botão para sair da conta
            self.logoutButton = customtkinter.CTkButton(
                master, text="Sair", command=self.logout)
            self.logoutButton.grid(row=3, column=0,
                                   padx=20, pady=20,
                                   sticky="ew")

    def logout(self):
        UserDAO.logout()
        self.app.show_AuthTabView()
