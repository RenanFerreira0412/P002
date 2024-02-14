import 'package:flutter/material.dart';
import 'package:frontend/utils/utils.dart';

class WelcomeHeader extends StatelessWidget implements PreferredSizeWidget {
  const WelcomeHeader({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return AppBar(
      actions: [
        ElevatedButton(onPressed: () {}, child: const Text('Ao vivo agora')),
        Utils.addHorizontalSpace(10),
        IconButton(onPressed: () {}, icon: const Icon(Icons.person_rounded))
      ],
    );
  }

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);
}
