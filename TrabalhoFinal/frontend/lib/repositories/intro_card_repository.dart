import 'package:frontend/models/intro_card_data.dart';

class IntroCardRepository {
  static List<IntroCardData> cardData = [
    IntroCardData(
        imagePath: 'lib/assets/image/supporter.png',
        label: 'Acompanhe os campeonatos que estão acontecendo agora'),
    IntroCardData(
        imagePath: 'lib/assets/image/arena.png',
        label: 'Torneios de voleibol, futsal, basquete e muito mais'),
    IntroCardData(
        imagePath: 'lib/assets/image/league.png',
        label:
            'Cadastre os seus torneios para que outras equipes possam participar')
  ];
}
