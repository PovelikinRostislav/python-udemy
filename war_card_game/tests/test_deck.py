import unittest
from wargame.deck import Deck
from wargame.card import ranks, Card

class TestDeck(unittest.TestCase):
    def test_cards_in_default_deck(self):
        # Check that default deck has 4 cards of each rank
        deck = Deck()
        ranks_dict = {rank:4 for rank in ranks}

        for card in deck.cards:
            ranks_dict[card.rank] -= 1

        self.assertFalse(any(ranks_dict.values()))

    def test_cards_in_custom_deck(self):
        list_of_cards = [Card(rank) for rank in ranks]
        deck = Deck(list_of_cards)

        self.assertEquals(len(list_of_cards), 0)
        self.assertEquals(len(deck.cards), len(ranks))
