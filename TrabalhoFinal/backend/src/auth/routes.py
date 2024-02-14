from flask import jsonify, request, Response, json
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo.collection import Collection
from bson import ObjectId, json_util
from ..models.user import User
from ..utils.utils import Utils
from ..extensions import pymongo
from src.auth import auth

from datetime import datetime

# referência a coleção dos usuários
users: Collection = pymongo.db.users


@auth.route('/app/user', methods=['GET'])
def get_user():
    """
    receber usuário atual
    """

    currentUser = users.find_one({'is_active': True})
    response = json_util.dumps(currentUser)
    return Response(response, mimetype="application/json")


@auth.route('/app/entrar', methods=['POST', 'PUT'])
def login():
    """
    Login do usuário
    """

    data = request.get_json()
    email = data['email']
    password = data['password']

    # buscando o usuário no banco de dados
    user = users.find_one({"email": email})

    # verificando se o usuário não foi encontrado ou
    # se a senha está errada
    if not user or not check_password_hash(user['password'], password):
        return jsonify({"message": "E-mail ou senha inválidos."}), 404

    # atualizando o status de ativação do usuário
    users.update_one({"_id": ObjectId(user['_id'])}, {
        "$set": {"is_active": True}})

    return jsonify({"message": f"Seja bem-vindo {user['username']}."}), 200


@auth.route('/app/cadastro', methods=['POST'])
def register():
    """
    Cadastro de usuários
    """

    data = request.get_json()

    # procurando pelo usuário
    user = users.find_one({"email": data["email"]})

    # verificando se o email já foi cadastrado
    if user:
        return jsonify({"message": "Este endereço de email já existe!"}), 404

    # 'escondendo' a senha informada pelo usuário
    hashed_password = generate_password_hash(data["password"])

    # criando um novo usuário
    user_obj = User(
        username=data['username'],
        email=data['email'],
        password=hashed_password,
        createdAt=datetime.now()
    )

    new_user = Utils.obj_to_json(user_obj)

    # registrando o usuário
    users.insert_one(new_user)

    return jsonify({"message": "Usuário cadastrado com sucesso!"}), 200


@auth.route('/app/desconectar/<user_id>', methods=['PUT'])
def logout(user_id):
    """
    Sair da conta do usuário
    """

    # atualizando o status de ativação do usuário
    users.update_one({"_id": ObjectId(user_id)}, {
        "$set": {"is_active": False}})

    return jsonify({"message": "Desconectado(a) com sucesso!"}), 200


@auth.route('/app/deletar/<user_id>', methods=['DELETE'])
def delete(user_id):
    """
    Deletar conta do usuário
    """

    # deletando os dados associados ao usuário

    # deletando o usuário
    users.delete_one({"_id": ObjectId(user_id)})

    return jsonify({"message": "Sua conta foi deletada com sucesso!"}), 200


@auth.route('/app/verificar/usuario', methods=['POST'])
def check_user():
    """
    Verificando o email do usuário
    """

    data = request.get_json()

    user = users.find_one({'email': data['email']})

    # verificando se o usuário foi encontrado!
    if user:
        return jsonify({'message': 'Prossiga informando sua nova senha.', "userId": str(user['_id'])}), 200

    return jsonify({"message": "Este endereço de email não foi encontrado."}), 404


@auth.route('/app/senha/mudar/<user_id>', methods=['POST', 'PUT'])
def resetPassword(user_id):
    """
    Mudança de senha do usuário
    """

    data = request.get_json()

    # 'escondendo' a senha informada pelo usuário
    hashed_password = generate_password_hash(data["password"])

    # atualizando a senha do usuário
    users.update_one({"_id": ObjectId(user_id)}, {
                     "$set": {"password": hashed_password}})

    return jsonify({"message": "Sua senha foi atualizada com sucesso! Realize novamente o seu login."}), 200
