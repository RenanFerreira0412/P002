from tkinter import *
from tkinter import ttk
from data.product_dao import ProductDAO
from data.inventory_dao import InventoryDAO
from models.product import Product
from models.inventory import Inventory
import customtkinter


class InventoryUI(customtkinter.CTkTabview):
    def __init__(self, master):
        super().__init__(master)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)
        self.products = [item[1] for item in ProductDAO.find()]

        # bool para controlar a edição e criação do inventário
        self.is_editing = False

        # produto
        self.inventory = None

        # campo data
        self.date = customtkinter.CTkEntry(
            master, placeholder_text="Data (dd/mm/yyyy)")
        self.date.grid(row=1, column=0, columnspan=2,
                       padx=20, pady=10, sticky="ew")

        # campo seleção de produtos
        self.product = customtkinter.CTkComboBox(master, values=self.products,
                                                 command=self.combobox_callback)
        self.product.grid(row=2, column=0,
                          padx=20, pady=10,
                          sticky="ew")
        self.product.set(self.products[0])

        # campo valor unitário
        self.value = customtkinter.CTkEntry(
            master, placeholder_text="Valor unitário")
        self.value.grid(row=3, column=0, columnspan=2,
                        padx=20, pady=10, sticky="ew")

        # campo data de validade
        self.data_validation = customtkinter.CTkEntry(
            master, placeholder_text="Validade (dd/mm/yyyy)")
        self.data_validation.grid(row=4, column=0, columnspan=2,
                                  padx=20, pady=10, sticky="ew")

        # campo número de entradas
        self.n_entries = customtkinter.CTkEntry(
            master, placeholder_text="Quantidade de entradas")
        self.n_entries.grid(row=5, column=0, columnspan=2,
                            padx=20, pady=10, sticky="ew")

        # campo número de saídas
        self.n_outputs = customtkinter.CTkEntry(
            master, placeholder_text="Quantidade de saídas")
        self.n_outputs.grid(row=6, column=0, columnspan=2,
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

    def combobox_callback(self, choice):
        print("combobox dropdown clicked:", choice)

    def set_vals(self):
        if self.is_editing:
            self.date.insert(0, self.inventory.date)
            self.product.set(self.inventory.product)
            self.value.insert(0, self.inventory.value)
            self.data_validation.insert(0, self.inventory.data_validation)
            self.n_entries.insert(0, self.inventory.n_entries)
            self.n_outputs.insert(0, self.inventory.n_outputs)


        self.create_treeview()

    def delete(self):
        InventoryDAO.deleteOne(inventoryId=self.inventory.id)

        self.is_editing = False

        message = "Produto deletado do inventário com sucesso!"

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
            inventory = item['values']
            print('inventário selecionado ', inventory)
            self.inventory = Inventory(
                *inventory[1:len(inventory)], id=inventory[0])

            self.enable_del_btn()

    def create_treeview(self):
        # produtos
        inventories = InventoryDAO.find()
        print("Todos os produtos do inventário ", inventories)
        # estilo
        self.style = ttk.Style()
        self.style.configure(
            "Treeview", foreground="black", background="white")

        # define columns
        columns = ('id', 'date', 'product', 'value', 'data_validation', 'n_entries', 'n_outputs',
                   'total_val_entries', 'total_val_outputs', 'daily_balance_number', 'daily_balance_total_val')

        self.tree = ttk.Treeview(
            self.master, columns=columns, show='headings', style="Treeview")

        # define headings
        self.tree.heading('id', text='ID')
        self.tree.heading('date', text='Data')
        self.tree.heading('product', text='Produto')
        self.tree.heading('value', text='Valor unitário')
        self.tree.heading('data_validation', text='Validade')
        self.tree.heading('n_entries', text='Qtd. Entradas')
        self.tree.heading('n_outputs', text='Qtd. Saídas')
        self.tree.heading('total_val_entries', text='Valor total entradas')
        self.tree.heading('total_val_outputs', text='Valor total saídas')
        self.tree.heading('daily_balance_number', text='Qtd. Saldo Diário')
        self.tree.heading('daily_balance_total_val', text='Qtd. Saldo Total')

        # inserindo os inventários na tabela
        for inventory in inventories:
            self.tree.insert('', END, values=inventory)

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        self.tree.grid(row=0, column=0, padx=20, pady=10,
                       sticky='nsew', columnspan=2)

        # add a scrollbar
        self.scrollbar = customtkinter.CTkScrollbar(
            self.master, orientation=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=2, sticky='ns')

    def cleanForm(self):
        self.date.delete(0, END)
        self.value.delete(0, END)
        self.data_validation.delete(0, END)
        self.n_entries.delete(0, END)
        self.n_outputs.delete(0, END)

    def save(self):
        # dados do formulário
        date = self.date.get()
        product = self.product.get()
        value = self.value.get()
        data_validation = self.data_validation.get()
        n_entries = self.n_entries.get()
        n_outputs = self.n_outputs.get()

        message = ""

        data = {
            "date": date,
            "product": product,
            "value": value,
            "data_validation": data_validation,
            "n_entries": n_entries,
            "n_outputs": n_outputs
        }

        is_valid = all(data.values())

        if is_valid:
            # convertendo os valores
            value = float(value)
            n_entries = int(n_entries)
            n_outputs = int(n_outputs)

            # calculando o saldo diário
            total_val_entries = value*n_entries
            total_val_outputs = value*n_outputs
            daily_balance_number = n_entries-n_outputs
            daily_balance_total_val = total_val_entries-total_val_outputs

            # atualizando o dicionário com novas informações
            data["total_val_entries"] = f"{total_val_entries:.2f}"
            data["total_val_outputs"] = f"{total_val_outputs:.2f}"
            data["daily_balance_number"] = f"{daily_balance_number:.2f}"
            data["daily_balance_total_val"] = f"{daily_balance_total_val:.2f}"
            

            if self.is_editing:
                # atualizando o produto no inventário
                InventoryDAO.updateOne(
                    data=data, inventoryId=self.inventory.id)
                
                self.is_editing = False
            else:
                # inserindo um novo produto no inventário
                if InventoryDAO.insertOne(data=data):
                    message = "Produto cadastrado no inventário com sucesso!"
                else:
                    message = "Este produto já foi cadastrado no inventário!"

            self.cleanForm()
        else:
            message = "Preencha todos os campos!"

        self.message.configure(text=message)
        self.deleteBtn.configure(
            fg_color="#E53935", hover_color="#C62828", state="disabled")

        self.set_vals()
