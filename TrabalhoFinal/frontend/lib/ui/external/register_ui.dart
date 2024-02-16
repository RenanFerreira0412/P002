import 'package:flutter/material.dart';
import 'package:frontend/components/editor.dart';
import 'package:frontend/services/auth_service.dart';
import 'package:frontend/ui/external/widget/auth_button.dart';
import 'package:frontend/utils/validation.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';

class RegisterUI extends StatefulWidget {
  const RegisterUI({super.key});

  @override
  State<RegisterUI> createState() => _RegisterUIState();
}

class _RegisterUIState extends State<RegisterUI> {
  // controladores
  final _username = TextEditingController();
  final _email = TextEditingController();
  final _password = TextEditingController();
  final _confirmPassword = TextEditingController();

  final _formkey = GlobalKey<FormState>();

  bool loading = false;

  String passwordVal = "";

  @override
  void initState() {
    super.initState();
    if (mounted) {
      updatePasswordVal();
    }
  }

  @override
  void dispose() {
    _username.dispose();
    _email.dispose();
    _password.dispose();
    _confirmPassword.dispose();
    super.dispose();
  }

  void updatePasswordVal() {
    _password.addListener(_passwordListener);
  }

  void _passwordListener() {
    setState(() {
      passwordVal = _password.text;
    });
  }

  register() async {
    setState(() => loading = true);
    try {
      await context
          .read<AuthService>()
          .register(context, _username.text, _email.text, _password.text);
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
                  'Crie sua conta',
                  textAlign: TextAlign.start,
                ),
                TextButton(
                    onPressed: () => context.go('/app/entrar'),
                    child: const Text('Voltar ao Login')),
                Form(
                    key: _formkey,
                    child: Column(
                      children: [
                        Editor(
                            controller: _username,
                            labelText: 'Nome',
                            hintText: 'Informe o seu nome.',
                            validator: FormValidation.validateField(),
                            maxLength: 50,
                            maxLines: 1,
                            isPasswordField: false,
                            keyboardType: TextInputType.name,
                            readOnly: false),
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
                        Editor(
                            controller: _confirmPassword,
                            labelText: 'Confirmar senha',
                            hintText: 'Repita a senha informada.',
                            validator: FormValidation.validateConfirmPassword(
                                passwordVal),
                            maxLength: 30,
                            maxLines: 1,
                            isPasswordField: true,
                            keyboardType: TextInputType.text,
                            readOnly: false),
                        AuthButton(
                            onPressed: () {
                              if (_formkey.currentState!.validate()) {
                                register();
                              }
                            },
                            loading: loading,
                            label: 'Cadastrar')
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
