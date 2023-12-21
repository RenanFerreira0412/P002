import uuid


class Product:
    def __init__(self, name, description, unit, maxStock, minStock, id=uuid.uuid4().hex):
        self.id = id
        self.name = name  # nome do produto
        self.description = description  # descrição do produto
        self.unit = unit  # unidade de consumo do produto
        self.maxStock = maxStock  # estoque máximo do produto
        self.minStock = minStock  # estoque mínimo do produto

    
    def update(self):
        pass
