import 'package:flutter/material.dart';

class IntroCard extends StatelessWidget {
  final String label;
  final String imagePath;

  const IntroCard({super.key, required this.label, required this.imagePath});

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
          border: Border.all(color: Colors.black),
          borderRadius: BorderRadius.circular(10)),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [Image.asset(imagePath), Text(label)],
      ),
    );
  }
}
