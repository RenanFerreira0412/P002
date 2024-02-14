import 'package:flutter/material.dart';
import 'package:frontend/services/auth_service.dart';
import 'package:frontend/ui/auth/login_form.dart';
import 'package:frontend/ui/auth/register_form.dart';
import 'package:frontend/ui/auth/reset_password_form.dart';
import 'package:provider/provider.dart';

class AuthUI extends StatefulWidget {
  const AuthUI({super.key});

  @override
  State<AuthUI> createState() => _AuthUIState();
}

class _AuthUIState extends State<AuthUI> {
  // Gerenciador dos formulários
  final formLoginKey = GlobalKey<FormState>();
  final formRegisterKey = GlobalKey<FormState>();
  final formResetPasswordKey = GlobalKey<FormState>();

  // Controladores
  final name = TextEditingController();
  final emailLogin = TextEditingController();
  final passwordLogin = TextEditingController();
  final emailRegister = TextEditingController();
  final passwordRegister = TextEditingController();
  final confirmPassword = TextEditingController();
  final emailResetPassword = TextEditingController();

  // Variáveis de Controle
  bool isLogin = true;
  bool isResetPasswordForm = false;
  bool loading = false;

  late String title;
  late String actionButton;
  late String toggleButton;
  late String toggleResetPasswordButton;
  late Widget form;

  @override
  void initState() {
    super.initState();
    setFormAction(true, false);
  }

  setFormAction(bool acao, bool forgotPswForm) {
    setState(() {
      isLogin = acao;
      isResetPasswordForm = forgotPswForm;

      if (isLogin) {
        if (isResetPasswordForm) {
          title = 'Recuperar senha';
          actionButton = 'Enviar';
          toggleButton = 'Ainda não tem conta? Cadastre-se agora.';
          toggleResetPasswordButton = "Voltar";
          form = ResetPasswordForm(
              email: emailResetPassword, formKey: formResetPasswordKey);
        } else {
          title = 'Bem vindo';
          actionButton = 'Login';
          toggleButton = 'Ainda não tem conta? Cadastre-se agora.';
          toggleResetPasswordButton = 'Esqueceu sua senha ?';
          form = LoginForm(
              email: emailLogin,
              password: passwordLogin,
              formKey: formLoginKey);
        }
      } else {
        title = 'Crie sua conta';
        actionButton = 'Cadastrar';
        toggleButton = 'Voltar ao Login.';
        form = RegisterForm(
            name: name,
            email: emailRegister,
            password: passwordRegister,
            confirmPassword: confirmPassword,
            formKey: formRegisterKey);
      }
    });
  }

  login() async {
    setState(() => loading = true);
    try {
      await context
          .read<AuthService>()
          .login(emailLogin.text, passwordLogin.text);
    } catch (e) {
      setState(() => loading = false);
    }
  }

  register() async {
    setState(() => loading = true);
    try {
      await context
          .read<AuthService>()
          .register(name.text, emailRegister.text, passwordRegister.text);
    } catch (e) {
      setState(() => loading = false);
    }
  }

  resetPassword() async {
    try {
      await context.read<AuthService>().resetPassword(emailResetPassword.text);
    } catch (e) {
      debugPrint('$e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Center(
            child: Container(
              constraints: const BoxConstraints(
                maxWidth: 500,
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    title,
                  ),
                  if (!isResetPasswordForm) ...[
                    Padding(
                      padding: const EdgeInsets.symmetric(vertical: 15),
                      child: TextButton(
                        onPressed: () => setFormAction(!isLogin, false),
                        child: Text(toggleButton),
                      ),
                    )
                  ] else ...[
                    const Padding(
                      padding: EdgeInsets.symmetric(vertical: 15),
                      child: Text(
                        'Um link de recuperação de senha será enviado para o endereço de e-mail fornecido por você.',
                        textAlign: TextAlign.start,
                      ),
                    )
                  ],
                  form,
                  if (isLogin) ...[
                    Align(
                      alignment: Alignment.centerRight,
                      child: TextButton(
                          onPressed: () =>
                              setFormAction(isLogin, !isResetPasswordForm),
                          child: Text(
                            toggleResetPasswordButton,
                            textAlign: TextAlign.center,
                          )),
                    ),
                  ],
                  Padding(
                    padding: const EdgeInsets.symmetric(vertical: 25),
                    child: ElevatedButton(
                      style: ElevatedButton.styleFrom(
                          elevation: 2,
                          shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(5))),
                      onPressed: () {
                        if (isLogin) {
                          if (isResetPasswordForm) {
                            if (formResetPasswordKey.currentState!.validate()) {
                              resetPassword();
                              cleanForm();
                            }
                          } else {
                            if (formLoginKey.currentState!.validate()) {
                              login();
                              cleanForm();
                            }
                          }
                        } else {
                          if (formRegisterKey.currentState!.validate()) {
                            register();
                            cleanForm();
                          }
                        }
                      },
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: (loading)
                            ? [
                                const Padding(
                                  padding: EdgeInsets.all(15),
                                  child: SizedBox(
                                    width: 24,
                                    height: 24,
                                    child: CircularProgressIndicator(
                                      color: Colors.white,
                                    ),
                                  ),
                                )
                              ]
                            : [
                                const Icon(Icons.check),
                                Padding(
                                  padding: const EdgeInsets.all(15),
                                  child: Text(
                                    actionButton,
                                  ),
                                ),
                              ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }

  void cleanForm() {
    name.clear();
    emailLogin.clear();
    passwordLogin.clear();
    emailRegister.clear();
    passwordRegister.clear();
    confirmPassword.clear();
    emailResetPassword.clear();
  }
}
