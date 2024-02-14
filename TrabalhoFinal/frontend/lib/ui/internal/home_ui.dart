import 'package:flutter/material.dart';
import 'package:frontend/services/auth_service.dart';
import 'package:provider/provider.dart';

class HomeUI extends StatelessWidget {
  const HomeUI({super.key});

  @override
  Widget build(BuildContext context) {
    AuthService auth = Provider.of<AuthService>(context);
    return Scaffold(
      body: SingleChildScrollView(
          child: Column(
        children: [
          ElevatedButton(
              onPressed: () => auth.logout(), child: const Text('Desconectar'))
        ],
      )),
    );
  }
}
