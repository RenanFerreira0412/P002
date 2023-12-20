import customtkinter
from .signin_ui import SignInUI
from .signup_ui import SignUpUI


class AuthTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # criando as tabs
        self.add("Login")
        self.add("Cadastro")

        # adicionando os widgets das tabs
        self.signin = SignInUI(master=self.tab("Login"), app=master)
        self.signup = SignUpUI(master=self.tab("Cadastro"), app=master)
