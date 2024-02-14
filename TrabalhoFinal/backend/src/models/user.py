class User:
    """
    classe que representa os usuário do sistema
    """

    def __init__(self, username, email, password, createdAt, _id=None):
        self.id = _id
        self.createdAt = createdAt
        self.username = username
        self.email = email
        self.password = password
        self.is_active = True
