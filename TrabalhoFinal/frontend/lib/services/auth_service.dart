import 'package:flutter/material.dart';
import 'package:frontend/api/constants.dart';
import 'package:frontend/models/user.dart';
import 'package:frontend/utils/utils.dart';
import 'package:go_router/go_router.dart';
import 'dart:convert';

import 'package:http/http.dart' as http;

class AuthService extends ChangeNotifier {
  User? usuario;
  String? verifiedUserId;
  bool isLoading = true;

  AuthService() {
    _authCheck();
  }

  // verificação do status de autenticação do usuário
  _authCheck() async {
    var url = Uri.parse('${ApiConstants.baseUrl}${ApiConstants.userEndpoint}');

    await http.get(url).then((response) {
      var data = json.decode(response.body);
      usuario = (data == null) ? null : User.fromJson(data);
      isLoading = false;
      notifyListeners();
    }).catchError((error) {
      debugPrint("Erro na solicitação HTTP: $error");
    });
  }

  // login do usuário
  login(BuildContext context, String email, String password) async {
    var url = Uri.parse('${ApiConstants.baseUrl}${ApiConstants.loginEndpoint}');

    await http
        .post(
      url,
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, String>{'email': email, 'password': password}),
    )
        .then((response) {
      var data = json.decode(response.body);
      Utils.schowSnackBar(data['message']);
      // navegando para o widget que controla o status de autenticação
      if (response.statusCode == 200) {
        context.go('/');
      }

      _authCheck();
    }).catchError((error) {
      debugPrint("Erro na solicitação HTTP: $error");
    });
  }

  // cadastro do usuário
  register(BuildContext context, String username, String email,
      String password) async {
    var url =
        Uri.parse('${ApiConstants.baseUrl}${ApiConstants.registerEndpoint}');

    await http
        .post(url,
            headers: <String, String>{
              'Content-Type': 'application/json; charset=UTF-8',
            },
            body: jsonEncode(<String, String>{
              'username': username,
              'email': email,
              'password': password
            }))
        .then((response) {
      var data = json.decode(response.body);
      Utils.schowSnackBar(data['message']);
      // navegando para o widget que controla o status de autenticação
      if (response.statusCode == 200) {
        context.go('/');
      }

      _authCheck();
    }).catchError((error) {
      debugPrint("Erro na solicitação HTTP: $error");
    });
  }

  // desconectar usuário
  logout() async {
    var url = Uri.parse(
        '${ApiConstants.baseUrl}${ApiConstants.logoutEndpoint}/${usuario!.id}');

    await http.put(url).then((response) {
      var data = json.decode(response.body);
      Utils.schowSnackBar(data['message']);
      _authCheck();
    }).catchError((error) {
      debugPrint("Erro na solicitação HTTP: $error");
    });
  }

  // verificar usuário
  verifyUser(BuildContext context, String email) async {
    var url =
        Uri.parse('${ApiConstants.baseUrl}${ApiConstants.verifyUserEndpoint}');

    await http
        .post(url,
            headers: <String, String>{
              'Content-Type': 'application/json; charset=UTF-8',
            },
            body: jsonEncode(<String, String>{
              'email': email,
            }))
        .then((response) {
      var data = json.decode(response.body);

      Utils.schowSnackBar(data['message']);

      // navegando para a tela de mudança de senha
      if (response.statusCode == 200) {
        // id do usuário verificado
        verifiedUserId = data['userId'];

        context.go('/app/mudarsenha');
      }

      notifyListeners();
    }).catchError((error) {
      debugPrint("Erro na solicitação HTTP: $error");
    });
  }

  // mudança de senha
  resetPassword(String password) async {
    var url =
        Uri.parse('${ApiConstants.baseUrl}${ApiConstants.changePwdEndpoint}');

    await http
        .post(url,
            headers: <String, String>{
              'Content-Type': 'application/json; charset=UTF-8',
            },
            body: jsonEncode(<String, String>{
              'password': password,
              'userId': verifiedUserId!,
            }))
        .then((response) {
      var data = json.decode(response.body);
      Utils.schowSnackBar(data['message']);
      notifyListeners();
    }).catchError((error) {
      debugPrint("Erro na solicitação HTTP: $error");
    });
  }
}
