from tkinter import *
from data.user_dao import UserDAO
import customtkinter


class SignUpUI(customtkinter.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        # campo de nome
        self.name = customtkinter.CTkEntry(master, placeholder_text="Nome")
        self.name.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        # campo de email
        self.email = customtkinter.CTkEntry(master, placeholder_text="E-mail")
        self.email.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        # campo de senha
        self.password = customtkinter.CTkEntry(
            master, placeholder_text="Senha")
        self.password.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        # botão de cadastro
        self.signUpButton = customtkinter.CTkButton(
            master, text="Cadastrar", command=self.signUp)
        self.signUpButton.grid(row=3, column=0,
                               padx=20, pady=20,
                               sticky="ew")

        # mensagem de aviso
        self.message = customtkinter.CTkLabel(
            master, text="", fg_color="transparent")
        self.message.grid(row=4, column=0, padx=20, pady=10)

    # métodos

    def cleanForm(self):
        self.name.delete(0, END)
        self.email.delete(0, END)
        self.password.delete(0, END)

    def signUp(self):
        print("Cadastrando")
        name = self.name.get()
        email = self.email.get()
        password = self.password.get()

        message = ""

        if not email or not password or not name:
            message = "Campo(s) obrigatório(s))!"
        else:

            if UserDAO.signUp(name=name, email=email, password=password):
                self.app.show_InternalTabView()
            else:
                message = "Esse email já está sendo utilizado."

            # limpando o formulário
            self.cleanForm()

        # exibindo a mensagem
        self.message.configure(text=message)
