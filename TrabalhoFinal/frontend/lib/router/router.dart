import 'package:frontend/ui/external/forgot_password_ui.dart';
import 'package:frontend/ui/external/login_ui.dart';
import 'package:frontend/ui/external/register_ui.dart';
import 'package:frontend/ui/external/reset_password_ui.dart';
import 'package:frontend/ui/internal/home_ui.dart';
import 'package:frontend/widget/auth_check.dart';
import 'package:go_router/go_router.dart';

final GoRouter route = GoRouter(
  routes: <RouteBase>[
    GoRoute(
        path: '/',
        builder: (context, state) {
          return const AuthCheck();
        },
        routes: [
          GoRoute(
            path: 'app/entrar',
            builder: (context, state) {
              return const LoginUI();
            },
          ),
          GoRoute(
            path: 'app/cadastro',
            builder: (context, state) {
              return const RegisterUI();
            },
          ),
          GoRoute(
            path: 'app/esqueciasenha',
            builder: (context, state) {
              return const ForgotPasswordUI();
            },
          ),
          GoRoute(
            path: 'app/mudarsenha',
            builder: (context, state) {
              return const ResetPasswordUI();
            },
          ),
          GoRoute(
            path: 'app/casa',
            builder: (context, state) {
              return const HomeUI();
            },
          ),
        ]),
  ],
);
