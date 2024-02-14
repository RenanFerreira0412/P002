import 'package:flutter/material.dart';

class LeagueSearchSection extends StatelessWidget {
  const LeagueSearchSection({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [_titles()],
    );
  }

  Widget _titles() {
    return Column(
      children: [
        const Text('Procure por torneios próximos a você'),
        const Text(
            'Abaixo, encontrará cada uma das ligas que estão abertas para inscrição. Verifique a modalidade das ligas disponíveis para poder se inscrever.'),
        RichText(
            text: const TextSpan(children: <TextSpan>[
          TextSpan(
              text:
                  'Se tiver alguma dúvida ou precisar de ajuda para se registar, '),
          TextSpan(text: 'contacte-nos.')
        ])),
      ],
    );
  }
}
