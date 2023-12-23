import customtkinter
from tkinter import ttk
from .add_products_ui import AddProductsUI
from .inventory_ui import InventoryUI
from .profile_ui import ProfileUI

class InternalTabView(customtkinter.CTkTabview):
    def __init__(self, master, currentUser=None, **kwargs):
        super().__init__(master, **kwargs)

        # criando as tabs
        self.add("Cadastro de\n Produtos")
        self.add("Inventário")
        self.add("Perfil")

        # estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # adicionando os widgets das tabs
        self.add_products = AddProductsUI(master=self.tab("Cadastro de\n Produtos"))
        self.inventory = InventoryUI(master=self.tab("Inventário"))
        self.profile = ProfileUI(master=self.tab("Perfil"), app=master, currentUser=currentUser)
