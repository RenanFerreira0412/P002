import 'package:flutter/material.dart';
import 'package:frontend/api/constants.dart';
import 'package:frontend/models/user.dart';
import 'package:frontend/utils/utils.dart';
import 'dart:convert';

import 'package:http/http.dart' as http;

Future<http.Response> createAlbum(String title) {
  return http.post(
    Uri.parse('https://jsonplaceholder.typicode.com/albums'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, String>{
      'title': title,
    }),
  );
}

class AuthService extends ChangeNotifier {
  User? usuario;
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
  login(String email, String password) async {
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
      _authCheck();
    }).catchError((error) {
      debugPrint("Erro na solicitação HTTP: $error");
    });
  }

  // cadastro do usuário
  register(String username, String email, String password) async {
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

  // mudança de senha
  resetPassword(String email) async {}
}
