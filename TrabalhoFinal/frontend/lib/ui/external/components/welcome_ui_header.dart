import 'package:flutter/material.dart';
import 'package:frontend/utils/responsive.dart';
import 'package:frontend/utils/utils.dart';
import 'package:go_router/go_router.dart';

class WelcomeHeader extends StatelessWidget implements PreferredSizeWidget {
  const WelcomeHeader({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return AppBar(
      actions: [
        if (!Responsive.isMobile(context)) ...[
          Tooltip(
            message: 'Acompanhar os jogos ao vivo',
            child: ElevatedButton(
              onPressed: () {},
              child: const Text('Ao vivo agora'),
            ),
          ),
          Utils.addHorizontalSpace(10),
        ],
        IconButton(
          onPressed: () => context.go('/app/entrar'),
          icon: const Icon(Icons.person_rounded),
          tooltip: 'Autenticação',
        )
      ],
    );
  }

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}
