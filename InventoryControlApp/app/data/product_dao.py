from models.product import Product
import json
import pandas as pd
import uuid

class ProductDAO:
    # referência a coleção products
    product_instance = "database/collections/products.txt"

    @classmethod
    def find(cls):
        # Abre o arquivo para leitura e escrita
        with open(cls.product_instance, "r") as file:
            # Lê o conteúdo atual do arquivo como uma lista de objetos JSON

            products = [json.loads(line) for line in file]

            # Converte o dicionário para um DataFrame
            df = pd.DataFrame.from_dict(products)

            # Converte o DataFrame para uma lista de listas
            all_products = df.values.tolist()

            file.close()

        return all_products

    @classmethod
    def insertOne(cls, data):
        id = uuid.uuid4().hex

        new_product = vars(Product(id=id,name=data['name'], description=data['description'],
                           unit=data['unit'], maxStock=data['maxStock'], minStock=data['minStock']))
        
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
        product = vars(Product(id=productId, name=data['name'], description=data['description'],
                               unit=data['unit'], maxStock=data['maxStock'], minStock=data['minStock']))

        print(data)
        print(productId)

        # lendo o arquivo
        with open(cls.product_instance, "r") as f:

            # lendo cada linha do arquivo
            products = f.readlines()

        # escrevendo no arquivo
        with open(cls.product_instance, "w") as f:

            for line in products:
                # escrevendo os produtos
                line_data = line
                if json.loads(line)['id'] == productId:
                    line_data = json.dumps(product) + '\n'

                f.write(line_data)

            f.close()

    @classmethod
    def deleteOne(cls, productId):
        print("Estou deletando um dado")
        # lendo o arquivo
        with open(cls.product_instance, "r") as f:

            # lendo cada linha do arquivo
            data = f.readlines()

        # escrevendo no arquivo
        with open(cls.product_instance, "w") as f:

            for line in data:

                # escrevendo apenas os produtos que não serão deletados
                if json.loads(line)['id'] != productId:
                    f.write(line)

            f.close()
