<h1 align="center">poker-h</h1>

# About

## What is this?

This is a module that will help you create a poker game.

## Library Features

Creating deck, hand, board as a list

Print the above and any lists

Print what combos are on the table

Print outs

### Features of printing outs

Outs are calculated exclusively using a table taken from Roy Rounder's book

Outs can only be counted after using `check_hand.combos()`


----------


# Getting Started

## Installation

	pip install poker-h


## Usage


Using this module is very simple and intuitive.

First we have to import everything from the module

``` python
from poker_h import *
```

Examples of all functions:

Creating a deck or hand

``` python
d = deck.deck()
h = deck.hand(d)
```


To create a board, we must specify a number, this is the number of cards that the program will distribute to the table

``` python
number = 5 #any number
b = deck.board(d, number)
```


To print deck, hand, board, or any other cards in the list

``` python
print(deck.print_cards(d))
```


To print the combos and how many outs you have (be sure to write hand and board)

``` python
print(check_hand.combos(h, b))
print(check_hand.outs())
```


## Example
``` python
from main import *

d = deck.deck()

b = deck.board(d, 5)
h = deck.hand(d)

print(f"Cards in hand: {deck.print_cards(h)}")
print(f"Cards on the table: {deck.print_cards(b)}")

print(f"\nCombination with cards: {check_hand.combos(h, b)}")
print(f"How many outs: {check_hand.outs()}")
```


----------


## Developer
Gimer

GitHub: [link](https://github.com/windgim)
