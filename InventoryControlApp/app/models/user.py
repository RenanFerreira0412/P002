from datetime import datetime


class User:
    """
    classe para representar os usuários do sistema
    """

    def __init__(self, uid, name, email, password, createdAt=str(datetime.now())):
        self.uid = uid  # id
        self.name = name  # nome
        self.email = email  # email
        self.password = password  # senha
        self.createdAt = createdAt  # data de criação

    def __str__(self) -> str:
        return f"{self.uid}-{self.name}"
