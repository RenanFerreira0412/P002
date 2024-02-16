import 'package:flutter/material.dart';
import 'package:frontend/components/editor.dart';
import 'package:frontend/services/auth_service.dart';
import 'package:frontend/ui/external/widget/auth_button.dart';
import 'package:frontend/utils/validation.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';

class LoginUI extends StatefulWidget {
  const LoginUI({super.key});

  @override
  State<LoginUI> createState() => _LoginUIState();
}

class _LoginUIState extends State<LoginUI> {
  // controladores
  final _email = TextEditingController();
  final _password = TextEditingController();

  final _formkey = GlobalKey<FormState>();

  bool loading = false;

  @override
  void dispose() {
    _email.dispose();
    _password.dispose();
    super.dispose();
  }

  login() async {
    setState(() => loading = true);
    try {
      await context
          .read<AuthService>()
          .login(context, _email.text, _password.text);
    } catch (e) {
      setState(() => loading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Center(
          child: Container(
            constraints: const BoxConstraints(maxWidth: 500),
            child: Column(
              children: [
                const Text(
                  'Bem-Vindo!',
                  textAlign: TextAlign.start,
                ),
                TextButton(
                    onPressed: () => context.go('/app/cadastro'),
                    child: const Text('Novo usuário? Cadastre-se.')),
                Form(
                    key: _formkey,
                    child: Column(
                      children: [
                        Editor(
                            controller: _email,
                            labelText: 'Email',
                            hintText: 'Informe o seu email.',
                            validator: FormValidation.validateEmail(),
                            maxLength: 50,
                            maxLines: 1,
                            isPasswordField: false,
                            keyboardType: TextInputType.emailAddress,
                            readOnly: false),
                        Editor(
                            controller: _password,
                            labelText: 'Senha',
                            hintText: 'Informe a sua senha.',
                            validator: FormValidation.validateField(),
                            maxLength: 30,
                            maxLines: 1,
                            isPasswordField: true,
                            keyboardType: TextInputType.text,
                            readOnly: false),
                        Align(
                          alignment: Alignment.bottomRight,
                          child: TextButton(
                              onPressed: () => context.go('/app/esqueciasenha'),
                              child: const Text('Esqueceu sua senha?')),
                        ),
                        AuthButton(
                            onPressed: () {
                              if (_formkey.currentState!.validate()) {
                                login();
                              }
                            },
                            loading: loading,
                            label: 'Entrar')
                      ],
                    )),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
