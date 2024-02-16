import 'package:flutter/material.dart';
import 'package:frontend/components/editor.dart';
import 'package:frontend/services/auth_service.dart';
import 'package:frontend/ui/external/widget/auth_button.dart';
import 'package:frontend/utils/validation.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';

class ForgotPasswordUI extends StatefulWidget {
  const ForgotPasswordUI({super.key});

  @override
  State<ForgotPasswordUI> createState() => _ForgotPasswordUIState();
}

class _ForgotPasswordUIState extends State<ForgotPasswordUI> {
  // controladores
  final _email = TextEditingController();

  final _formkey = GlobalKey<FormState>();

  bool loading = false;

  @override
  void dispose() {
    _email.dispose();
    super.dispose();
  }

  verifyUser() async {
    setState(() => loading = true);
    try {
      await context.read<AuthService>().verifyUser(context, _email.text);
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
                  'Recuperar senha',
                  textAlign: TextAlign.start,
                ),
                const Text('Informe o seu endereço de e-mail'),
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
                        TextButton(
                            onPressed: () => context.go('/app/entrar'),
                            child: const Text('Voltar')),
                        AuthButton(
                            onPressed: () {
                              if (_formkey.currentState!.validate()) {
                                verifyUser();
                              }
                            },
                            loading: loading,
                            label: 'Verificar')
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
