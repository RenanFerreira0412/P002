import 'package:flutter/material.dart';

class AuthButton extends StatefulWidget {
  final VoidCallback onPressed;
  final String label;
  final bool loading;

  const AuthButton(
      {super.key,
      required this.onPressed,
      required this.loading,
      required this.label});

  @override
  State<AuthButton> createState() => _AuthButtonState();
}

class _AuthButtonState extends State<AuthButton> {
  late bool _loading;

  @override
  void initState() {
    _loading = widget.loading;
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 25),
      child: ElevatedButton(
        style: ElevatedButton.styleFrom(
            elevation: 2,
            shape:
                RoundedRectangleBorder(borderRadius: BorderRadius.circular(5))),
        onPressed: widget.onPressed,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: (_loading)
              ? [
                  const Padding(
                    padding: EdgeInsets.all(15),
                    child: SizedBox(
                      width: 24,
                      height: 24,
                      child: CircularProgressIndicator(
                        color: Colors.white,
                      ),
                    ),
                  )
                ]
              : [
                  const Icon(Icons.check),
                  Padding(
                    padding: const EdgeInsets.all(15),
                    child: Text(
                      widget.label,
                    ),
                  ),
                ],
        ),
      ),
    );
  }
}
