import 'package:flutter/material.dart';
import 'package:frontend/repositories/intro_card_repository.dart';
import 'package:frontend/ui/external/widget/intro_card.dart';

class IntroductionSection extends StatelessWidget {
  const IntroductionSection({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [_titles(), _cards()],
    );
  }

  Widget _titles() {
    return const Column(
      children: [
        Text("LIGAS ESPORTIVAS"),
        Text("Esportes, dedicação e entretenimento")
      ],
    );
  }

  Widget _cards() {
    return GridView.builder(
      shrinkWrap: true,
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 3,
      ),
      itemCount: IntroCardRepository.cardData.length,
      itemBuilder: (context, index) {
        var data = IntroCardRepository.cardData[index];
        return IntroCard(
          label: data.label,
          imagePath: data.imagePath,
        );
      },
    );
  }
}
