import 'package:flutter/material.dart';

final theme = ThemeData(colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple));

class Home extends StatelessWidget {
  final List<String> items;
  const Home(this.items);
  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      onWillPop: () async => false,
      child: SingleChildScrollView(
        child: Column(
          children: items.map((i) => Card(child: Card(child: Text(i)))).toList(),
        ),
      ),
    );
  }
}

final dot = Container(width: 8, height: 8, decoration: BoxDecoration(shape: BoxShape.circle));
final t = MediaQuery(data: MediaQueryData(textScaler: TextScaler.noScaling), child: Text('Hi'));
