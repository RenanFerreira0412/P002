from tkinter import *
from data.product_dao import ProductDAO
import customtkinter


class ProductsTable(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values

        total_rows = len(self.values)
        total_columns = len(self.values[0])

        for i in range(total_rows):
            for j in range(1, total_columns):

                self.e = customtkinter.CTkEntry(self)

                self.e.grid(row=i, column=j, padx=20, pady=10, sticky="ew")
                self.e.insert(END, self.values[i][j])


class AddProductsUI(customtkinter.CTkTabview):
    def __init__(self, master):
        super().__init__(master)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        # bool para controlar a edição e criação de produtos
        self.is_editing = False

        # produto
        self.product = None


        # campo nome
        self.name = customtkinter.CTkEntry(
            master, placeholder_text="Nome do produto")
        self.name.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        # campo descrição
        self.description = customtkinter.CTkEntry(
            master, placeholder_text="Descrição")
        self.description.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        # campo unidade de consumo
        self.unit = customtkinter.CTkEntry(
            master, placeholder_text="Unidade de consumo")
        self.unit.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        # campo estoque mínimo
        self.minStock = customtkinter.CTkEntry(
            master, placeholder_text="Estoque mínimo")
        self.minStock.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        # campo estoque máximo
        self.maxStock = customtkinter.CTkEntry(
            master, placeholder_text="Estoque máximo")
        self.maxStock.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

        # botão de login
        self.saveButton = customtkinter.CTkButton(
            master, text="Salvar", command=self.save)
        self.saveButton.grid(row=5, column=0,
                             padx=20, pady=20,
                             sticky="ew")

        # mensagem de aviso
        self.message = customtkinter.CTkLabel(
            master, text="", fg_color="transparent")
        self.message.grid(row=6, column=0, padx=20, pady=10)

        self.set_vals()

    def cleanForm(self):
        self.name.delete(0, END)
        self.description.delete(0, END)
        self.unit.delete(0, END)
        self.minStock.delete(0, END)
        self.maxStock.delete(0, END)

    def set_vals(self):
        if self.is_editing:
            self.name.insert(0, self.product.name)
            self.description.insert(0, self.product.description)
            self.unit.insert(0, self.product.unit)
            self.minStock.insert(0, self.product.minStock)
            self.maxStock.insert(0, self.product.maxStock)
        else:
            self.cleanForm()

        print(ProductDAO.find())

        #self.create_table()

    def create_table(self):
        products = ProductDAO.find()
        print(products)

        total_rows = len(products)
        total_columns = len(products[0])

        for i in range(total_rows):
            for j in range(1, total_columns):

                self.e = customtkinter.CTkEntry(self.master)

                self.e.grid(row=i, column=j)
                self.e.insert(END, products[i][j])

    def save(self):
        # dados do formulário
        name = self.name.get()
        description = self.description.get()
        unit = self.unit.get()
        minStock = self.minStock.get()
        maxStock = self.maxStock.get()

        message = ""

        data = {
            "name": name,
            "description": description,
            "unit": unit,
            "minStock": minStock,
            "maxStock": maxStock
        }

        if self.is_editing:
            # inserindo um novo produto
            if ProductDAO.updateOne(data=data, productId=self.product.id):
                message = "Produto atualizado com sucesso!"
            else:
                message = "Produto não encontrado!"

            self.is_editing = False
        else:
            # inserindo um novo produto
            if ProductDAO.insertOne(data=data):
                message = "Produto cadastrado com sucesso!"
            else:
                message = "Este produto já foi cadastrado!"

        self.message.configure(text=message)

        self.set_vals()
