import 'package:flutter/material.dart';
import 'package:frontend/router/router.dart';
import 'package:frontend/utils/utils.dart';

class SportsLeague extends StatelessWidget {
  const SportsLeague({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      title: 'Flutter Demo',
      debugShowCheckedModeBanner: false,
      scaffoldMessengerKey: Utils.messengerKey,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      routerConfig: route,
    );
  }
}
