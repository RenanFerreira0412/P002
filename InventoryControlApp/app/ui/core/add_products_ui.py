from tkinter import *
from tkinter import ttk
from data.product_dao import ProductDAO
from models.product import Product
import customtkinter


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
        self.name.grid(row=2, column=0, columnspan=2,
                       padx=20, pady=10, sticky="ew")

        # campo descrição
        self.description = customtkinter.CTkEntry(
            master, placeholder_text="Descrição")
        self.description.grid(row=3, column=0, columnspan=2,
                              padx=20, pady=10, sticky="ew")

        # campo unidade de consumo
        self.unit = customtkinter.CTkEntry(
            master, placeholder_text="Unidade de consumo")
        self.unit.grid(row=4, column=0, columnspan=2,
                       padx=20, pady=10, sticky="ew")

        # campo estoque mínimo
        self.minStock = customtkinter.CTkEntry(
            master, placeholder_text="Estoque mínimo")
        self.minStock.grid(row=5, column=0, columnspan=2,
                           padx=20, pady=10, sticky="ew")

        # campo estoque máximo
        self.maxStock = customtkinter.CTkEntry(
            master, placeholder_text="Estoque máximo")
        self.maxStock.grid(row=6, column=0, columnspan=2,
                           padx=20, pady=10, sticky="ew")

        # botão de salvar
        self.saveButton = customtkinter.CTkButton(
            master, text="Salvar", command=self.save)
        self.saveButton.grid(row=7, column=0, columnspan=2,
                             padx=20, pady=20,
                             sticky="ew")

        self.deleteBtn = customtkinter.CTkButton(
            self.master, text="Deletar", command=self.delete)
        self.deleteBtn.grid(row=8, column=0,
                            padx=20, pady=10,
                            sticky="ew")
        self.deleteBtn.configure(
            fg_color="#E53935", hover_color="#C62828", state="disabled")

        # mensagem de aviso
        self.message = customtkinter.CTkLabel(
            master, text="", fg_color="transparent")
        self.message.grid(row=9, column=0, columnspan=2, padx=20, pady=10)

        
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

        self.create_treeview()

    def delete(self):
        ProductDAO.deleteOne(productId=self.product.id)

        self.is_editing = False

        message = "Produto deletado com sucesso!"

        self.cleanForm()
        self.set_vals()

        self.message.configure(text=message)
        self.deleteBtn.configure(
            fg_color="#E53935", hover_color="#C62828", state="disabled")

    def enable_del_btn(self):
        self.deleteBtn.configure(
            fg_color="#E53935", hover_color="#C62828", state="normal")

        self.is_editing = True
        self.set_vals()

    def item_selected(self, event):
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            product = item['values']

            self.product = Product(*product[1:len(product)], id=product[0])

            self.enable_del_btn()

    def create_treeview(self):
        # produtos
        products = ProductDAO.find()

        # define columns
        columns = ('id', 'name', 'description', 'unit', 'minStock', 'maxStock')

        self.tree = ttk.Treeview(
            self.master, columns=columns, show='headings')

        # define headings
        self.tree.heading('id', text='ID')
        self.tree.heading('name', text='Nome')
        self.tree.heading('description', text='Descrição')
        self.tree.heading('unit', text='Unidade de consumo')
        self.tree.heading('minStock', text='Estoque mínimo')
        self.tree.heading('maxStock', text='Estoque máximo')

        # inserindo os produtos na tabela
        for product in products:
            self.tree.insert('', END, values=product)

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        self.tree.grid(row=0, column=0, padx=20, pady=10,
                       sticky='nsew', columnspan=2)

        # add a scrollbar
        self.scrollbar = customtkinter.CTkScrollbar(
            self.master, orientation=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=2, sticky='ns')

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

        is_valid = all(data.values())

        if is_valid:
            if self.is_editing:
                # atualizando o produto
                ProductDAO.updateOne(data=data, productId=self.product.id)

                self.is_editing = False
            else:
                # inserindo um novo produto
                if ProductDAO.insertOne(data=data):
                    message = "Produto cadastrado com sucesso!"
                else:
                    message = "Este produto já foi cadastrado!"

            self.cleanForm()
        else:
            message = "Preencha todos os campos!"

        self.message.configure(text=message)
        self.deleteBtn.configure(
            fg_color="#E53935", hover_color="#C62828", state="disabled")

        self.set_vals()
