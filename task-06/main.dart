iimport 'package:bunny/bunny_game.dart';
import 'package:flame/game.dart';
import 'package:flutter/material.dart';
import 'package:bunny/helpers/navigation_keys.dart';

void main() {
  final game = BunnyGame();
  runApp(
    MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        body: Stack(
          children: [
            GameWidget(
              game: game,
            ),
            Align(
              alignment: Alignment.bottomRight,
              child: NavigationKeys(
                onDirectionChanged: game.onArrowKeyChanged,
              ),
            ),
          ],
        ),
      ),
    ),
  );
}




