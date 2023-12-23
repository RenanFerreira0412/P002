from models.inventory import Inventory
import json
import pandas as pd
import uuid


class InventoryDAO:
    # referência a coleção products
    inventory_instance = "database/collections/inventories.txt"

    @classmethod
    def find(cls):
        # Abre o arquivo para leitura e escrita
        with open(cls.inventory_instance, "r") as file:
            # Lê o conteúdo atual do arquivo como uma lista de objetos JSON
            inventories = [json.loads(line) for line in file]

            # Converte o dicionário para um DataFrame
            df = pd.DataFrame.from_dict(inventories)

            # Converte o DataFrame para uma lista de listas
            all_inventories = df.values.tolist()

            file.close()

        print(all_inventories)

        return all_inventories

    @classmethod
    def insertOne(cls, data):
        id = uuid.uuid4().hex

        new_inventory = vars(Inventory(id=id,
                                       date=data['date'],
                                       product=data['product'],
                                       value=data['value'],
                                       data_validation=data['data_validation'],
                                       n_entries=data['n_entries'],
                                       n_outputs=data['n_outputs'],
                                       total_val_entries=data['total_val_entries'],
                                       total_val_outputs=data['total_val_outputs'],
                                       daily_balance_number=data['daily_balance_number'],
                                       daily_balance_total_val=data['daily_balance_total_val']))

        print('dados recebidos ', data)
        print(data['date'])
        print('objeto inventário ', new_inventory)
        # Abre o arquivo para leitura e escrita
        with open(cls.inventory_instance, "r+") as file:
            # Lê o conteúdo atual do arquivo como uma lista de objetos JSON
            product_already_selected = [json.loads(
                line)['product'] for line in file]

            # Verificando se o usuário já selecionou o produto
            if data['product'] in product_already_selected:
                return False

            file.write(json.dumps(new_inventory) + '\n')

            file.close()

            return True

    @classmethod
    def updateOne(cls, data, inventoryId):
        inventory = vars(Inventory(id=inventoryId,
                                   date=data['date'],
                                   product=data['product'],
                                   value=data['value'],
                                   data_validation=data['data_validation'],
                                   n_entries=data['n_entries'],
                                   n_outputs=data['n_outputs'],
                                   total_val_entries=data['total_val_entries'],
                                   total_val_outputs=data['total_val_outputs'],
                                   daily_balance_number=data['daily_balance_number'],
                                   daily_balance_total_val=data['daily_balance_total_val']))

        # lendo o arquivo
        with open(cls.inventory_instance, "r") as f:

            # lendo cada linha do arquivo
            inventories = f.readlines()

        # escrevendo no arquivo
        with open(cls.inventory_instance, "w") as f:

            for line in inventories:
                # escrevendo os produtos no inventário
                line_data = line
                if json.loads(line)['id'] == inventoryId:
                    line_data = json.dumps(inventory) + '\n'

                f.write(line_data)

            f.close()

    @classmethod
    def deleteOne(cls, inventoryId):
        print("Estou deletando um dado")
        # lendo o arquivo
        with open(cls.inventory_instance, "r") as f:

            # lendo cada linha do arquivo
            data = f.readlines()

        # escrevendo no arquivo
        with open(cls.inventory_instance, "w") as f:

            for line in data:

                # escrevendo apenas os inventários que não serão deletados
                if json.loads(line)['id'] != inventoryId:
                    f.write(line)

            f.close()
