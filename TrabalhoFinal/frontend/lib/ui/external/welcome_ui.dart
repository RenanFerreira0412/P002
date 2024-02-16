import 'package:flutter/material.dart';
import 'package:frontend/ui/external/components/introduction_section.dart';
import 'package:frontend/ui/external/components/league_search_section.dart';
import 'package:frontend/ui/external/components/welcome_ui_header.dart';
import 'package:frontend/ui/external/widget/drawer_option.dart';
import 'package:frontend/utils/responsive.dart';

class WelcomeUI extends StatefulWidget {
  const WelcomeUI({super.key});

  @override
  State<WelcomeUI> createState() => _WelcomeUIState();
}

class _WelcomeUIState extends State<WelcomeUI> {
  int _selectedIndex = 0;

  static const List<Widget> sections = [
    IntroductionSection(),
    LeagueSearchSection()
  ];

  static List<String> options = ['Início', 'Procurar Ligas'];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: const WelcomeHeader(),
      body: SingleChildScrollView(
        child: Container(
          child: sections[_selectedIndex],
        ),
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            const DrawerHeader(
              decoration: BoxDecoration(
                color: Colors.blue,
              ),
              child: Text('Ligas Esportivas'),
            ),
            ...List.generate(
              options.length,
              (index) {
                return DrawerOption(
                  label: options[index],
                  onTap: () {
                    // atualiza o estado do app
                    _onItemTapped(index);
                    // fecha o drawer
                    Navigator.pop(context);
                  },
                  selected: _selectedIndex == index,
                );
              },
            ),
            if (Responsive.isMobile(context)) ...[
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 18),
                child: Tooltip(
                  message: 'Acompanhar os jogos ao vivo',
                  child: ElevatedButton(
                    onPressed: () {},
                    child: const Text('Ao vivo agora'),
                  ),
                ),
              ),
            ]
          ],
        ),
      ),
    );
  }
}
