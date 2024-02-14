import customtkinter
from ui.auth.auth_tab import AuthTabView
from ui.core.internal_tab import InternalTabView
from data.user_dao import UserDAO


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Controle de Estoque")
        self.geometry("1000x700")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # tab das telas de autenticação
        self.auth_tab_view = AuthTabView(master=self)
        self.auth_tab_view.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # tab das telas internas
        self.internal_tab_view = InternalTabView(master=self)
        self.internal_tab_view.grid(
            row=0, column=0, padx=20, pady=20, sticky="ew")

        # exibe inicialmente a tab das telas de autenticação
        self.show_AuthTabView()

    def show_AuthTabView(self):
        # Exibe a tab das telas de autenticação e esconde o de telas internas
        self.auth_tab_view.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.internal_tab_view.grid_forget()

    def show_InternalTabView(self):
        # Exibe a tab das telas internas e esconde o de autenticação
        self.internal_tab_view = InternalTabView(
            master=self, currentUser=UserDAO.currentUser)
        self.internal_tab_view.grid(
            row=0, column=0, padx=20, pady=20, sticky="ew")
        self.auth_tab_view.grid_forget()


app = App()
app.mainloop()
