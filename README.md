# PokerH Library #

## What is this? ##

This is a library that will help you create a poker game.

## Library Features ##

Creating deck, hand, board as a list

Print the above and any lists

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

	d = deck.deck()
	h = deck.hand(d)


To create a board, we must specify a number, this is the number of cards that the program will distribute to the table

	number = 5 #any number
	b = deck.board(d, number)


To print deck, hand, board, or any other cards in the list

	print(deck.print_cards(d))


To print the combos and how many outs you have (be sure to write hand and board)

	print(check_hand.combos(h, b))
	print(check_hand.outs(h, b))


----------


## Developer ##
Gimer

GitHub: [link](https://github.com/windgim)