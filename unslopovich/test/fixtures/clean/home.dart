import 'package:flutter/material.dart';

final theme = ThemeData(colorScheme: ColorScheme.fromSeed(seedColor: Color(0xFF1B6E5A)));

class Home extends StatelessWidget {
  final List<String> items;
  const Home(this.items);
  @override
  Widget build(BuildContext context) {
    return PopScope(
      canPop: true,
      child: ListView.builder(
        itemCount: items.length,
        itemBuilder: (context, i) => ListTile(title: Text(items[i])),
      ),
    );
  }
}
