import 'package:flutter/material.dart';
import 'package:frontend/repositories/intro_card_repository.dart';
import 'package:frontend/ui/external/widget/intro_card.dart';
import 'package:frontend/utils/responsive.dart';
import 'package:frontend/utils/utils.dart';

class IntroductionSection extends StatelessWidget {
  const IntroductionSection({super.key});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [_titles(), Utils.addVerticalSpace(20), _cards(context)],
      ),
    );
  }

  Widget _titles() {
    return const Column(
      children: [
        Text(
          "LIGAS ESPORTIVAS",
          textAlign: TextAlign.center,
        ),
        Text(
          "Esportes, dedicação e entretenimento",
          textAlign: TextAlign.center,
        )
      ],
    );
  }

  Widget _cards(BuildContext context) {
    return GridView.builder(
      shrinkWrap: true,
      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: Responsive.isDesktop(context)
              ? 3
              : Responsive.isTablet(context)
                  ? 2
                  : 1,
          mainAxisSpacing: 30,
          crossAxisSpacing: 30,
          childAspectRatio: 1.5),
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
