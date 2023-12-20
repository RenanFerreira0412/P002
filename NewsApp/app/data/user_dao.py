from models.user import User
import json
import uuid


class UserDAO:
    # usuário atual
    currentUser = None

    # referência a coleção users
    user_instance = "database/collections/users.txt"

    @classmethod
    def signUp(cls, name, email, password):
        # gerando um UUID aleatório
        uid = uuid.uuid4()

        new_user = vars(User(uid=uid.hex, name=name, email=email,
                        password=password))

        # Abre o arquivo para leitura e escrita
        with open(cls.user_instance, "r+") as file:
            # Lê o conteúdo atual do arquivo como uma lista de objetos JSON
            email_already_in_use = [json.loads(
                line)['email'] for line in file]

            # Verificando se o usuário informou um email já em uso
            if email in email_already_in_use:
                return False

            cls.currentUser = User(**new_user)

            file.write(json.dumps(new_user) + '\n')

            file.close()

            return True

    @classmethod
    def signIn(cls, email, password):
        # Abre o arquivo para leitura e escrita
        with open(cls.user_instance, "r") as file:
            # Lê o conteúdo atual do arquivo como uma lista de objetos JSON
            user = [json.loads(line) for line in file if email in json.loads(
                line)['email'] and password in json.loads(line)['password']]

            # Verificando se o usuário informou um email já em uso
            if len(user) == 0:
                return False

            cls.currentUser = User(**user[0])

            file.close()

            return True
        
    @classmethod
    def logout(cls):
        cls.currentUser = None
