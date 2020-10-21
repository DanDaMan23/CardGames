import random

class Card:

    def __init__(self, suit, value):
        suits = ("hearts", "diamonds", "clubs", "spades")
        values = [str(i) for i in range(1, 14)]
        values[0] = "A"
        values[12] = "K"
        values[11] = "Q"
        values[10] = "J"
        values = tuple(values)

        if suit not in suits:
            raise Exception("Invalid suit")
        elif value not in values:
            raise Exception("Invalid value")

        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
        suits = ("hearts", "diamonds", "clubs", "spades")
        values = [str(i) for i in range(1, 14)]
        values[0] = "A"
        values[12] = "K"
        values[11] = "Q"
        values[10] = "J"
        values = tuple(values)

        self.cards = [Card(suit, value) for suit in suits for value in values]

    def count(self):
        return len(self.cards)

    def _deal(self, number):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")

        self.cards = self.cards[:-number]

    def shuffle(self):
        if self.count() != 52:
            raise ValueError("Only full decks can be shuffled")

        random.shuffle(self.cards)

        return self.cards

    def deal_card(self):
        card = self.cards[self.count() - 1]

        self._deal(1)

        return card

    def deal_hand(self, num):
        hand = self.cards[-num:]
        self._deal(num)
        return hand

    def __repr__(self):
        return f"Deck of {self.count()} cards"              
