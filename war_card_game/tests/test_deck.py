import unittest
from wargame.deck import Deck
from wargame.card import ranks

class TestDeck(unittest.TestCase):
    def test_cards_in_default_deck(self):
        # Check that default deck has 4 cards of each rank
        deck = Deck()
        ranks_dict = {rank:4 for rank in ranks}

        for card in deck.cards:
            ranks_dict[card.rank] -= 1

        self.assertFalse(any(ranks_dict.values()))

