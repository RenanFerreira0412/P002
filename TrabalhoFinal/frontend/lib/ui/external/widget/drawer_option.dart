import 'package:flutter/material.dart';

class DrawerOption extends StatelessWidget {
  final String label;
  final VoidCallback onTap;
  final bool selected;

  const DrawerOption(
      {super.key,
      required this.label,
      required this.onTap,
      required this.selected});

  @override
  Widget build(BuildContext context) {
    return ListTile(
      title: Text(label),
      selected: selected,
      onTap: onTap,
    );
  }
}
