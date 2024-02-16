import 'package:flutter/material.dart';
import 'package:frontend/utils/utils.dart';

class LeagueSearchSection extends StatelessWidget {
  const LeagueSearchSection({super.key});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [_titles()],
      ),
    );
  }

  Widget _titles() {
    return Column(
      children: [
        const Text(
          'Procure por torneios próximos a você',
          textAlign: TextAlign.center,
        ),
        Utils.addVerticalSpace(10),
        const Text(
          'Abaixo, encontrará cada uma das ligas que estão abertas para inscrição. Verifique a modalidade das ligas disponíveis para poder se inscrever.',
          textAlign: TextAlign.center,
        ),
        Utils.addVerticalSpace(20),
        RichText(
            textAlign: TextAlign.center,
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
