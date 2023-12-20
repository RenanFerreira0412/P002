from tkinter import *
from data.user_dao import UserDAO
import customtkinter



class SignInUI(customtkinter.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        # campo de email
        self.email = customtkinter.CTkEntry(master, placeholder_text="E-mail")
        self.email.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        # campo de senha
        self.password = customtkinter.CTkEntry(
            master, placeholder_text="Senha")
        self.password.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        # botão de login
        self.signInButton = customtkinter.CTkButton(
            master, text="Entrar", command=self.signIn)
        self.signInButton.grid(row=2, column=0,
                               padx=20, pady=20,
                               sticky="ew")

        # mensagem de aviso
        self.message = customtkinter.CTkLabel(
            master, text="", fg_color="transparent")
        self.message.grid(row=3, column=0, padx=20, pady=10)

    # métodos

    def cleanForm(self):
        self.email.delete(0, END)
        self.password.delete(0, END)

    def signIn(self):

        email = self.email.get()
        password = self.password.get()

        message = ""

        if not email or not password:
            message = "Campo(s) obrigatório(s))!"
            print("Logando")
        else:

            if UserDAO.signIn(email=email, password=password):
                self.app.show_InternalTabView()
                message = ""
            else:
                message = "E-mail ou senha inválidos."

            # limpando o formulário
            self.cleanForm()

        print(message)
        self.message.configure(text=message)
