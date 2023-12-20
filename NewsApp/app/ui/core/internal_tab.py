import customtkinter
from .home_ui import HomeUI
from .profile_ui import ProfileUI


class InternalTabView(customtkinter.CTkTabview):
    def __init__(self, master, currentUser=None, **kwargs):
        super().__init__(master, **kwargs)

        # criando as tabs
        self.add("Início")
        self.add("Perfil")

        # adicionando os widgets das tabs
        self.home = HomeUI(master=self.tab("Início"))
        self.profile = ProfileUI(master=self.tab(
            "Perfil"), app=master, currentUser=currentUser)
