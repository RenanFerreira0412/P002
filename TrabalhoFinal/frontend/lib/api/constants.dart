import 'package:flutter_dotenv/flutter_dotenv.dart';

class ApiConstants {
  // url base
  static String baseUrl = dotenv.get('BASE_URL');

  // Endpoint com referência as coleções do banco de dados
  static String userEndpoint = dotenv.get('USER');

  // Endpoint para operações de autenticação
  static String loginEndpoint = dotenv.get('LOGIN');
  static String registerEndpoint = dotenv.get('REGISTER');
  static String logoutEndpoint = dotenv.get('LOGOUT');

  // Endpoint para operações CRUD
  static String createEndpoint = dotenv.get('CREATE');
  static String updateEndpoint = dotenv.get('UPDATE');
  static String deleteEndpoint = dotenv.get('DELETE');
}
