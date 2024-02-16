import 'package:flutter/material.dart';
import 'package:frontend/utils/utils.dart';

class IntroCard extends StatelessWidget {
  final String label;
  final String imagePath;

  const IntroCard({super.key, required this.label, required this.imagePath});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
          border: Border.all(color: Colors.black),
          borderRadius: BorderRadius.circular(10)),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Expanded(
            child: Image.asset(
              imagePath,
              fit: BoxFit.contain,
            ),
          ),
          Utils.addVerticalSpace(20),
          Text(
            label,
            textAlign: TextAlign.center,
          )
        ],
      ),
    );
  }
}
