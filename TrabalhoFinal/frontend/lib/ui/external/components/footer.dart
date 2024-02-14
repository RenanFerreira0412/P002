import 'package:flutter/material.dart';

class Footer extends StatelessWidget {
  const Footer({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Container(
        padding: const EdgeInsets.all(20),
        child: RichText(
            text: const TextSpan(children: <TextSpan>[
          TextSpan(text: 'Desenvolvido por '),
          TextSpan(text: 'Renan Ferreira')
        ])),
      ),
    );
  }
}
