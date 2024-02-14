from flask import Blueprint

auth = Blueprint('auth', __name__)

from src.auth import routes