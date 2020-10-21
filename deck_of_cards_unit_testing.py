import unittest
from deck_of_cards import Card, Deck

class CardUnitTest(unittest.TestCase):
    def test_card_repr(self):
        self.assertEqual(str(Card("hearts", "K")), "K of hearts")
        self.assertEqual(str(Card("spades", "A")), "A of spades")

    def test_card_exceptions(self):
        with self.assertRaises(Exception):
            Card("squares", "2")

        with self.assertRaises(Exception):
            Card("hearts", "P")


class DeckUnitTest(unittest.TestCase):
    def test_deck_repr(self):
        self.assertEqual(str(Deck()), "Deck of 52 cards")

    def test_deal_card(self):
        deck = Deck()
        card = Card("spades", "K")
        
        self.assertEqual(str(deck.deal_card()), str(card))

        card.value = "Q"

        self.assertEqual(str(deck.deal_card()), str(card))
        
    def test_count(self):
        deck = Deck()
        self.assertEqual(deck.count(), 52)

        deck.deal_card()

        self.assertEqual(deck.count(), 51)

    def deal_hand(self):
        deck = Deck()

        hand = ["J of spades", "Q of spades", "K of spades"]

        hand_delt = [str(card) for card in deck.deal_hand(3)]

        self.assertEqual(hand_delt, hand)

    def test_shuffle(self):
        ordered_deck = Deck()
        deck = Deck()

        deck.shuffle()

        self.assertTrue(ordered_deck.cards[0] != deck.cards[0] or ordered_deck.cards[1] != deck.cards[1] 
            or ordered_deck.cards[2] != deck.cards[2])

    def test_shuffle_exception(self):
        deck = Deck()

        deck.deal_hand(3)

        with self.assertRaises(ValueError):
            deck.shuffle()


if __name__ == "__main__":
    unittest.main()