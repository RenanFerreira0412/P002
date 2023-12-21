from models.product import Product
import json
import uuid
import pandas as pd


class ProductDAO:
    # referência a coleção products
    product_instance = "database/collections/products.txt"

    @classmethod
    def find(cls):
        # Abre o arquivo para leitura e escrita
        with open(cls.product_instance, "r") as file:
            # Lê o conteúdo atual do arquivo como uma lista de objetos JSON
            # products = [Product(**json.loads(line)) for line in file]
            products = [json.loads(line) for line in file]

            # Converte a lista de objetos JSON para uma string JSON
            json_data = json.dumps(products)

            # Convert JSON string to a Pandas DataFrame
            df = pd.read_json(json_data)

            # Convert Pandas DataFrame to a Python list
            all_products = df.values.tolist()

            print(all_products)

            file.close()

            return all_products

    @classmethod
    def insertOne(cls, data):
        new_product = vars(Product(name=data['name'], description=data['description'],
                           unit=data['unit'], maxStock=data['maxStock'], minStock=data['minStock']))
        print(new_product)
        # Abre o arquivo para leitura e escrita
        with open(cls.product_instance, "r+") as file:
            # Lê o conteúdo atual do arquivo como uma lista de objetos JSON
            product_already_exists = [json.loads(
                line)['name'] for line in file]

            # Verificando se o usuário informou um produto já cadastrado
            if data['name'] in product_already_exists:
                return False

            file.write(json.dumps(new_product) + '\n')

            file.close()

            return True

    @classmethod
    def updateOne(cls, data, productId):
        pass

    @classmethod
    def deleteOne(cls, productId):
        pass
