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

    def test_splitted_in_half_decks(self):
        initial_deck = Deck()
        expected_size = len(initial_deck.cards) // 2

        deck = initial_deck.split()

        self.assertEqual(len(initial_deck.cards), expected_size)
        self.assertEqual(len(deck.cards), expected_size)

    def test_ctor_throws_exception(self):
        with self.assertRaises(TypeError):
            Deck(3)
