import 'package:flutter/material.dart';
import 'package:frontend/components/editor.dart';
import 'package:frontend/services/auth_service.dart';
import 'package:frontend/ui/external/widget/auth_button.dart';
import 'package:frontend/utils/validation.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';

class ResetPasswordUI extends StatefulWidget {
  const ResetPasswordUI({super.key});

  @override
  State<ResetPasswordUI> createState() => _ResetPasswordUIState();
}

class _ResetPasswordUIState extends State<ResetPasswordUI> {
  // controladores
  final _password = TextEditingController();

  final _formkey = GlobalKey<FormState>();

  bool loading = false;

  @override
  void dispose() {
    _password.dispose();
    super.dispose();
  }

  resetPassword() async {
    setState(() => loading = true);
    try {
      await context.read<AuthService>().resetPassword(_password.text);
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
                  'Nova senha',
                  textAlign: TextAlign.start,
                ),
                const Text('Informe a sua nova senha'),
                Form(
                    key: _formkey,
                    child: Column(
                      children: [
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
                        TextButton(
                            onPressed: () => context.go('/app/entrar'),
                            child: const Text('Voltar')),
                        AuthButton(
                            onPressed: () {
                              if (_formkey.currentState!.validate()) {
                                resetPassword();
                                context.go('/app/entrar');
                              }
                            },
                            loading: loading,
                            label: 'Mudar')
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
