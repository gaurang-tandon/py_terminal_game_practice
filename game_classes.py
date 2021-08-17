"""Importing python's inbuilt random module"""
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    """defining Card class"""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    """defining Deck class"""

    def __init__(self):
        """Note this only happens once upon creation of a new Deck"""
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        """Shuffling the deck. Note this doesn't return anything"""
        random.shuffle(self.all_cards)

    def deal_one(self):
        """Note we remove one card from the list of all_cards"""
        return self.all_cards.pop()


class Player:
    """Defining player class"""

    def __init__(self, name):
        self.name = name
        # A new player has no cards
        self.all_cards = []

    def remove_one(self):
        """picking/removing ONE card from players hand
        Note we remove one card from the list of all_cards
        We state 0 to remove from the "top" of the deck
        We'll imagine index -1 as the bottom of the deck"""
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        """Adding new card/s to players hand"""
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
