---
week: A
title: Optional extras
lang: python
appendix: true
---

In this set of exercises, we will build a python/tkinter implementation of the puzzle game known as 2048.

> For research purposes, it may help to play a few rounds [online](https://play2048.co/).

This is a fairly complex project, so we will take our time.
In each exercise we will add more functionality and capability to our code, gradually building in complexity.

The game consists of a 4 &times; 4 grid of tiles.
Tiles are empty by default, but can contain numbers.
The game starts with two randomly selected tiles set to the number 2.

![final game](/assets/img/2048/final.png)

The rules of the 2048 game are fairly simple:

- Each turn, the player can choose to move up, down, left or right.
- Numbered tiles move as far as they can in the specified direction, displacing empty tiles as they go.
- If a tile is moved into another tile with the same number, the two tiles will merge, creating a new tile with double the value.
- Merging tiles scores points equal to the value of the new tile.
- After each turn, a randomly selected empty tile is set to either 2 or 4.
- The game ends when there are no further legal moves.

Don't worry if this doesn't make complete sense right now.
The details of the rules will become clear as we implement the necessary algorithms.
