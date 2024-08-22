# PokerH Library #

## What is this? ##

This is a library that will help you create a poker game.

## Library Features ##

Creating deck, hand, board as a list
Output the above as a string
Print what combos are on the table
Print outs

### Features of printing outs ###

Outs are calculated exclusively using a table taken from Roy Rounder's book


----------


## Using ##


Using this library is very simple and intuitive.

First we have to import everything from the library

	from poker_h import *


Examples of all functions:

Creating a deck or hand

	deck = deck.deck()
	hand = deck.hand()


To create a board, we must specify a number, this is the number of cards that the program will distribute to the table

	board = board(5)


To print a deck, hand or board use this code

	print(deck.print_deck(deck))
	print(deck.print_hand(hand))
	print(deck.print_board(board))


To print the combos and how many outs you have (be sure to write hand and board)

	print(check_hand.combos(hand, board))
	print(check_hand.outs(hand, board))


----------


## Developer ##
Gimer

GitHub: [link](https://github.com/windgim)